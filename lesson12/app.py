import sys
from downloader import Downloader

if __name__ == "__main__":
    # get package name from user input
    pkg_name = input("Please enter the package's name: ").strip()

    # check that package name is present
    if not pkg_name:
        print('Package name can\'t be empty')
        sys.exit()

    # download search result from api into (xml, csv, json) files
    downloader = Downloader(pkg_name)
    downloader.start_downloading()
