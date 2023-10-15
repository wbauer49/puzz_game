import sys
import pathlib
import pygbag.app


sys.argv = [pathlib.Path(__file__).parent, "main.py"]
pygbag.app.main()
