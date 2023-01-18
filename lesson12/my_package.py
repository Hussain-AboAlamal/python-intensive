from dataclasses import dataclass


@dataclass
class MyPackage:
    """A class that holds the package information
    """
    name: str
    version: str
    created: str
