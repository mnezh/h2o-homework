'''
Make sure datetime is converted to ISO representation for both
json.dump and flask.jsonify
'''
import datetime
from flask.json import JSONEncoder


def dump_serialize(datetime_object):
    if isinstance(datetime_object, datetime.datetime):
        return datetime_object.isoformat()
    raise TypeError("Type %s not serializable" % type(datetime_object))


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return datetime.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
