import datetime


def serialize(datetime_object):
    if isinstance(datetime_object, datetime.datetime):
        return datetime_object.isoformat()
    raise TypeError("Type %s not serializable" % type(datetime_object))
