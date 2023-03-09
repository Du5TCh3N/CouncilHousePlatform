from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import datetime
import os

from modeller import Modeller

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

def run_modeller(request):
    modeller = Modeller(startDate=datetime.date(2022, 1, 1), endDate=datetime.date(2022, 12, 31))
    message = "Model Simulation Completed"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(run_modeller, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()