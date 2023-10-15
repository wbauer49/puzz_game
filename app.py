import pathlib
from pygbag.app import main_run


class App:

    def __call__(self, *args, **kwargs):
        main_run(pathlib.Path(__file__).parent, "main.py")


app = App()
