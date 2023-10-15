import sys
import pathlib
import pygbag.app


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/octet-stream')])
    sys.argv = [pathlib.Path(__file__).parent, "main.py"]
    pygbag.app.main()
    return []
