from os import environ
from sanic import Sanic
from gino.ext.sanic import Gino


def sanic_config_manager(app: Sanic, prefix: str = "SANIC_"):
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value


def setup_database_creation_listener(app: Sanic, database: Gino):
    database.init_app(app)

    @app.listener("after_server_start")
    async def setup_database(app: Sanic, loop):
        await database.gino.create_all()

