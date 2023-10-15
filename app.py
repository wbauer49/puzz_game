import sys
import pathlib
import pygbag.app


def app(start_fn, environ):
    sys.argv = [pathlib.Path(__file__).parent, "main.py"]
    pygbag.app.main()
