import re

TAGS_SKIP = [
    "APIC:",
]

TAGS_REMOVE = [
    "TCOM",
    "TCON",
    "TCOP",
    "TCMP",
    "TENC",
    "TMED",
    "TPOS",
    "TPUB",
    "TRCK",
    "TSOT",
    "TSSE",
    "WFED",
    "WOAF",
    "WOAS",
    "WORS",
]

TAGS_REMOVE_PREFIX = (
    "COMM",
    "POPM",
    "USLT",
    "WCOM",
    "WOAR",
    "WXXX",
    "XXX",
)

# A regular expression that matches websites I download music from:
RE_WEBSITE = re.compile(r"""
    (?ix)                                    # IgnoreCase & Verbose
    \s*
    (?:\-|\|)?                               # Separators
    \s*
    (?:\[|\(|::)?                            # Block Starts
    (?:www.)?
    [\w]+                                    # Sitename
    \.
    (?:cc|com|in|info|se|site|me|mobi|pk)
    (?:\]|\)|::)?                            # Block Ends
""")
