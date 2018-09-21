# tagtool

Tagtool is a quick and easy-to-use tool for mass editing and cleaning metadata across your MP3 collection.

I wrote the initial version as a [simple script](https://github.com/dufferzafar/tagtool/blob/old/tagfix.py) that just worked. This tool later became an exercise in command line application design as I'd never done it before. It uses [docopt](http://docopt.org/) (along with some hackery to allow sub-commands)

## install

`pipsi install git+https://github.com/dufferzafar/tagtool#egg=tagtool`

You could also use [`pipsi`](https://github.com/mitsuhiko/pipsi) to install.

## usage

```
Usage:
    tagtool [--no-skip] <command> [<args>...]

Commands:
    replace     Perform regex replace on tags
    remove      Remove tag frames
    rename      Rename files to format: "%TrackTitle%.mp3"
    help        Read about a specific command

Options:
    --no-skip   Do not skip already tagged files
```

## commands

**`replace`**

```
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
```

**`remove`**

```
Remove tag frames.

Usage:
    tagtool remove  --frames=<tags> <file>...
                    [--prefix]

Options:
    <file>                       MP3 file(s) to process
    --frames=<frames>            Comma separated list of frames to remove
    --prefix                     Consider the list of frames as prefixes

Examples:
    tagtool remove --frames=APIC,COMM,USLT *.mp3
```

**`rename`**

```
Rename a file with its track title.

Usage:
    tagtool rename <file>...

Options:
    <file>                       MP3 file(s) to process

Examples:
    tagtool rename *.mp3
```

## tagfix

Tagfix is a script that uses the available tagtool commands as building blocks and performs multiple cleaning operation on files in one pass. If you download music from sites like [songspk](http://songspk.cc/) and [djmaza](http://www.djmaza.info/), this script is for you. It removes all mentions of these websites from the tags.
