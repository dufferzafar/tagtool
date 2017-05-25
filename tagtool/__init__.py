
from mutagen.mp3 import MP3

from . import commands
from .is_tagged import is_tagged


def _process(files, func, args, skip_tagged=False, needs_file=False):
    """ Apply func to ID3 tags of files. """

    for file in files:

        try:
            tags = MP3(file)
        except:
            print("Couldn't read: %s" % file)
            continue

        if (skip_tagged and is_tagged(tags)):
            print("Already tagged: %s " % file)
            continue

        print("Processing: %s" % file)

        if needs_file:
            func(file=file, tags=tags, **args)
        else:
            func(tags=tags, **args)
            tags.save()


def replace(files, **kwargs):
    _process(files, commands.replace, kwargs)


def remove(files, **kwargs):
    _process(files, commands.remove, kwargs)


def rename(files, skip_tagged=False, **kwargs):
    _process(files, commands.rename, kwargs,
             skip_tagged=skip_tagged, needs_file=True)


def case(files, **kwargs):
    _process(files, commands.case, kwargs)
