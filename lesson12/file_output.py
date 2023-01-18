from abc import ABC, abstractmethod
import csv
from enum import IntEnum
import xml.etree.ElementTree as ET
import json

from my_logger import MyLogger
from my_package import MyPackage


class FileOutputType(IntEnum):
    XML = 1
    JSON = 2
    CSV = 3

class FileOutput(ABC):
    """File output parent class
    """

    def __init__(self, file_path: str, data: list[MyPackage]) -> None:
        """Args:
            file_path (str): output file path
            data (list): rows to write them in the file
        """

        self.file_path = file_path
        self.data = data
        self.logger = MyLogger()

    @abstractmethod
    def export(self):
        """write data into file
        """
        pass


class JSONFileOutput(FileOutput):
    """Write data to file in JSON format
    """
    
    def export(self):
        # convert objects list to dictionary
        pkgsDict: list[dict] = [ob.__dict__ for ob in self.data]
        fcontent = {
            'packages': pkgsDict
        }

        # write data to file
        fcontent = json.dumps(fcontent, indent=2)
        with open(self.file_path, "w") as file:
            file.write(fcontent)


class CSVFileOutput(FileOutput):
    """Write data to file in CSV format
    """
    
    def export(self):
        # get table header from object keys
        header = list(self.data[0].__dict__.keys())

        # write data to file
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for x in self.data:
                writer.writerow([x.name, x.version, x.created])


class XMLFileOutput(FileOutput):
    """Write data to file in XML format
    """
    
    def export(self):
        # create parent element
        parent_elem = ET.Element('packages')
        ET.indent(parent_elem)

        # create child elements (package)
        for item in self.data:
            # create package element
            pkg_elem = ET.SubElement(parent_elem, 'package')
            pkg_elem.set('name', item.name)

            # create version child element for package
            child_elem = ET.SubElement(pkg_elem, 'version')
            child_elem.text = item.version

            # create created child element for package
            child_elem = ET.SubElement(pkg_elem, 'created')
            child_elem.text = item.created
        
        # write data to file
        tree = ET.ElementTree(parent_elem)
        ET.indent(tree, space="\t", level=0)
        tree.write(self.file_path)


def file_factory(type: int, file_path: str, data: list) -> CSVFileOutput | XMLFileOutput | JSONFileOutput:
    """Return file writer according to type

    Args:
        type (int): format of the exported file
        file_path (str): file path to store data
        data (list): data to write into file

    Returns:
        CSVFileOutput | XMLFileOutput | JSONFileOutput: file exporter object
    """

    # available file exports
    files = {
        FileOutputType.CSV: CSVFileOutput,
        FileOutputType.XML: XMLFileOutput,
        FileOutputType.JSON: JSONFileOutput,
    }

    try:
        return files[type](file_path, data)
    except Exception:
        raise
