import socket
from datetime import date, timedelta


def _get_ip():
    """
    :return: the actual ip of the local machine.
        This code figures out what source address would be used if some traffic
        were to be sent out to some well known address on the Internet. In this
        case, a Google DNS server is used, but the specific address does not
        matter much.  No traffic is actually sent.
    """
    try:
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _socket.connect(('8.8.8.8', 80))
        address, port = _socket.getsockname()
        _socket.close()
        return address
    except socket.error:
        return '127.0.0.1'

deploy_ip = _get_ip()


def get_date_range(start, end):
    """
    calculate date range
    :param start: string, yyyymmdd, start date
    :param end: string, yyyymmdd, end date
    :return: list, date string range list
    """
    date_range = []
    split_ymd = (lambda _d: (int(_d[:4]), int(_d[4:6]), int(_d[6:8])))
    date_start = date(*split_ymd(start))
    date_end = date(*split_ymd(end))

    while date_start <= date_end:
        date_range.append(str(date_start).replace('-', ''))
        date_start = timedelta(days=1) + date_start
    return date_range


