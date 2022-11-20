from datetime import datetime, timedelta


def now_timestamp():
    """
    helper function to get timestamp of the now
    """
    return datetime.now().replace(microsecond=0).timestamp()
