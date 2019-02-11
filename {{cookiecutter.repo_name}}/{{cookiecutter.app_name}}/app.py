from sanic import Sanic
from sanic.response import json as sanic_json
from {{cookiecutter.app_name}}.models import DATABASE
from {{cookiecutter.app_name}}.resources.user import UsersView, UserView
from {{cookiecutter.app_name}}.utils import setup_database_creation_listener

app = Sanic(__name__)

app.add_route(UsersView.as_view(), '/', version=1)
app.add_route(UserView.as_view(), '/<pk:int>', version=1)

setup_database_creation_listener(app, DATABASE)


@app.route("/")
async def default(request):
    return sanic_json({"message": "hello Sanic!"})
