import re

# Taken from flask_uuid: http://git.io/vmecV
UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

# Musicbrainz Recording ID
# https://picard.musicbrainz.org/docs/mappings/
ufid = u'UFID:http://musicbrainz.org'


def is_tagged(tags):
    """ Determine whether an MP3 file has been tagged by MusicBrainz Picard. """
    if ufid not in tags:
        return False
    else:
        return re.match(UUID_RE, tags[ufid].data.decode('ascii')) is not None
