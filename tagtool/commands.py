
import os
import re

from mutagen.id3 import TextFrame


def replace(tags, pattern, repl='', prune=True, frames=[], frames_skip=[]):
    r"""
    Perform regex replace on tags like artist name, track title etc.

    Usage:
        tagtool replace --pattern=<pattern> [--repl=<replacement>] <file>...
                        [--prune] [--frames=<tags>] [--frames_skip=<tags>]

    Options:
        <file>                       MP3 file(s) to process
        --pattern=<pattern>          Pattern to search for
        --repl=<replacement>         Replacement text
        --prune                      Remove empty frames
        --frames=<frames>            Comma separated list of frames to
                                     restrict replacement to
        --frames_skip=<frames>       Comma separated list of frames to skip

    Examples:
        tagtool replace --pattern='\s+\d+\s+' --repl='' --prune SomeSong.mp3 --frames_skip=TOPE,TIT2
    """

    for key in list(tags.keys()):

        if ((frames and key not in frames)
                or (frames_skip and key in frames_skip)
                or not isinstance(tags[key], TextFrame)):
            continue

        if re.search(pattern, str(tags[key])):
            sub = re.sub(pattern, repl, str(tags[key]))
            tags[key].text = [sub]
            if not sub and prune:
                del tags[key]


def remove(tags, frames, prefix=True):
    r"""
    Remove tag frames.

    Usage:
        tagtool remove  --frames=<tags> <file>...
                        [--prefix]

    Options:
        <file>                       MP3 file(s) to process
        --frames=<frames>            Comma separated list of frames to remove
        --prefix                     Consider the list of frames as prefixes

    Examples:
        tagtool remove --frames=APIC,COMM,USLT --prefix *.mp3
    """

    for key in list(tags.keys()):

        if prefix:
            if key.startswith(tuple(frames)):
                del tags[key]
        else:
            if key in frames:
                del tags[key]


# TODO: Support patterns like
# %title% - %artist%
def rename(file, tags):
    r"""
    Rename a file with it's track title.

    Usage:
        tagtool rename <file>...

    Options:
        <file>                       MP3 file(s) to process

    Examples:
        tagtool rename *.mp3
    """

    if 'TIT2' in tags:
        new_path = os.path.join(os.path.dirname(file),
                                "%s.mp3" % tags['TIT2'])
        os.rename(file, new_path)
        return new_path
    else:
        return file
