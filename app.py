import pathlib
import pygbag.app


async def app(environ, start_response=None, a=None):
    #start_response('200 OK', [('Content-Type', 'application/octet-stream')])
    await(pygbag.app.main_run(pathlib.Path(__file__).parent, "main.py"))
    return []
