#!/usr/bin/python2

"""ID3 Tag Fixer.

Usage:
  tagfix.py [options] <file>...
            [--remove=<tags>...]
            [--skip=<tags>...]
            [--rename]

Options:
  -h, --help        Show this screen.
  -v, --version     Show version.

"""

import os
import re

from docopt import docopt

from mutagen.mp3 import MP3
from mutagen.id3 import TextFrame

TAGS_REMOVE = [
    "COMM::'eng'",
    "TRCK", "TSOT", "TENC", "TPOS", "TCON", "TCOM",
    "WCOM", "WFED", "WOAF", "WOAR", "WOAS", "WORS",
]
TAGS_SKIP = [
    "APIC:",
]

# A regular expression that matches websites I download music from:
RE_WEBSITE = re.compile(r"""
    (?ix)                           # IgnoreCase & Verbose
    \s*                             #
    (?:\-|\|)?                      # Separators
    \s*                             #
    (?:\[|\()?                      # Block Starts
    (?:www.)?                       #
    [\w]+                           # Sitename
    \.                              #
    (?:com|info|site|pk|cc|se)      # Domains
    (?:\]|\))?                      # Block Ends
""")

if __name__ == '__main__':

    args = docopt(__doc__, version='ID3 Tag Fixer 0.3')

    TAGS_REMOVE.extend(args['--remove'])
    TAGS_SKIP.extend(args['--skip'])

    # Todo: Handle files other than mp3
    for file in args['<file>']:
        print(file)

        tags = MP3(file)

        for key in tags.keys():

            if key in TAGS_REMOVE or 'XXX' in key:
                del tags[key]
            elif key in TAGS_SKIP or not isinstance(tags[key], TextFrame):
                continue
            elif re.search(RE_WEBSITE, str(tags[key])):
                sub = re.sub(RE_WEBSITE, "", str(tags[key]))
                if sub:
                    tags[key].text = [sub]
                else:
                    del tags[key]

        # Fingers Crossed!
        tags.save()

        # Rename file with song title
        if args['--rename']:
            new_path = os.path.join(os.path.dirname(file),
                                    "%s.mp3" % tags['TIT2'])
            os.rename(file, new_path)
