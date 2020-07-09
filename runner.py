import os

from bottle import route, run, static_file


@route('/')
def catFeeder():
    return static_file('index.html', root=os.getcwd())


def get_ipaddr():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('google.com', 1))
        host, _ = s.getsockname()
        return host


if __name__ == '__main__':
    run(host=get_ipaddr(), port='8001', reloader=True)
