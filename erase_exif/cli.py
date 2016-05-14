from __future__ import absolute_import
import sys
from colorama import init, deinit, Fore
from erase_exif.erase import erase_exif


def main():
    init()

    try:
        filename, outfile = sys.argv[1:]

        erase_exif(filename, outfile)

        print(Fore.GREEN + 'Success!')
    except Exception as e:
        print(Fore.RED + 'Something went wrong')
        print(Fore.YELLOW + 'Example: $ erexif /path/to/filename.jpg output.jpg')

        sys.exit(1)

    deinit()
