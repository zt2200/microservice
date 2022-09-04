import json
from columbia_student_resource import ArtistResource


def t1():

    res = ArtistResource.get_by_key('nm0000158')
    print(json.dumps(res, indent=2, default=str))


t1()
