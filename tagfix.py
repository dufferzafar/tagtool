#!/usr/bin/python3

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

from is_tagged import is_tagged

from docopt import docopt

from mutagen.mp3 import MP3
from mutagen.id3 import TextFrame

from config import (
    RE_WEBSITE,
    TAGS_SKIP,
    TAGS_REMOVE,
    TAGS_REMOVE_PREFIX,
)


def _rename(args, file, tags):
    if args['--rename']:
        new_path = os.path.join(os.path.dirname(file),
                                "%s.mp3" % tags['TIT2'])
        os.rename(file, new_path)


if __name__ == '__main__':

    args = docopt(__doc__, version='ID3 Tag Fixer 0.3')

    TAGS_REMOVE.extend(args['--remove'])
    TAGS_SKIP.extend(args['--skip'])

    for file in args['<file>']:

        tags = MP3(file)
        if is_tagged(tags):
            _rename(args, file, tags)
            continue

        print(file)

        # Clean tags
        for key in tags.keys():

            if key in TAGS_REMOVE or key.startswith(TAGS_REMOVE_PREFIX):
                del tags[key]
            elif key in TAGS_SKIP or not isinstance(tags[key], TextFrame):
                continue
            elif re.search(RE_WEBSITE, str(tags[key])):
                sub = re.sub(RE_WEBSITE, "", str(tags[key]))
                if sub:
                    tags[key].text = [sub]
                else:
                    del tags[key]

        # Fingers crossed!
        tags.save()

        _rename(args, file, tags)
