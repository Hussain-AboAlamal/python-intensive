import os
import shutil
from file_output import FileOutputType, file_factory
from my_package import MyPackage
from my_logger import MyLogger

import requests
from bs4 import BeautifulSoup


API_URL = 'http://pypi.org/search?q='
OUTPUT_PATH = 'output'


class Fetching:
    '''Fetches data from api
    '''
    
    def __init__(self, pkg_name):
        """
        Args:
            pkg_name (str): the package's name to search for
        """
        self.__pkg_name = pkg_name
        self.logger = MyLogger()
        
    def fetch(self) -> str:
        """Fetch search result from web

        Returns:
            str: webpage html inner text
        """

        url = f'{API_URL}{self.__pkg_name}'
        self.logger.info(f'Requesting data from {url}')
        resp = requests.get(url)

        return resp.text


class Parsing:
    '''Extract data from html document'''

    def __init__(self):
        """
        Args:
            html_doc (string): result webpage html document
        """
        self.logger = MyLogger()

    def parse(self, html_doc) -> list[MyPackage]:
        """Parse html document package elements into list

        Returns:
            list[MyPackage]: extracted packages data
        """

        # initialize parser instance
        parser_type = 'html.parser'
        soup = BeautifulSoup(html_doc, parser_type)

        # extract title element for each package, for the first 10 packages
        titles = soup.select('.package-snippet__title')
        titles = iter(titles[:10])

        # extract package's name, version, date from package title element
        res = []
        for item in titles:
            name = item.select_one('.package-snippet__name').get_text()
            version = item.select_one('.package-snippet__version').get_text()
            created = item.select_one('.package-snippet__created').get_text().strip()

            self.logger.info(f'Parsing data for package {name}')
            pkg = MyPackage(name, version, created)
            res.append(pkg)
            
        return res


class Writing:
    '''Save search result into files'''
    
    def __init__(self):
        self.logger = MyLogger()

    def write(self, packages: list[MyPackage]):
        self.logger.info('Saving results to output files')

        # delete and re-create output directory
        if os.path.isdir(OUTPUT_PATH):
            shutil.rmtree(OUTPUT_PATH, ignore_errors=False, onerror=None)
        os.makedirs(OUTPUT_PATH)

        # export search result to xml file
        file_path = os.path.join(OUTPUT_PATH, 'result.xml')
        xml_export = file_factory(FileOutputType.XML, file_path, packages)
        xml_export.export()

        # export search result to csv file
        file_path = os.path.join(OUTPUT_PATH, 'result.csv')
        csv_export = file_factory(FileOutputType.CSV, file_path, packages)
        csv_export.export()

        # export search result to json file
        file_path = os.path.join(OUTPUT_PATH, 'result.json')
        json_export = file_factory(FileOutputType.JSON, file_path, packages)
        json_export.export()


class Downloader:
    '''Executes the whole downloading process'''
 
    def __init__(self, pkg_name):
        """
        Args:
            pkg_name (str): the package's name to downloads it's search result
        """

        self.pkg_name = pkg_name
        self.fetching = Fetching(pkg_name)
        self.parsing = Parsing()
        self.writing = Writing()
    
    def start_downloading(self):
        """start the process of downloading search result
        """

        html_doc = self.fetching.fetch()

        packages = self.parsing.parse(html_doc)
        # exit the app if there is no search result
        if len(packages) < 1:
            exit(f'There were no results for "{self.pkg_name}"')

        self.writing.write(packages)
