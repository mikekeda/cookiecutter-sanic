from sanic.exceptions import abort
from sanic.response import json as sanic_json
from sanic.views import HTTPMethodView

from asyncpg.exceptions import DataError
from marshmallow.exceptions import ValidationError

from {{cookiecutter.app_name}}.models.user import User
from {{cookiecutter.app_name}}.schemas.user import UserSchema

schema = UserSchema()


class UsersView(HTTPMethodView):
    # noinspection PyMethodMayBeStatic
    async def get(self, _):
        """ List of users. """
        users = await User.query.gino.all()
        return sanic_json([user.to_dict() for user in users], 200)

    # noinspection PyMethodMayBeStatic
    async def post(self, request):
        """ Create a new user. """
        user = {}
        try:
            data = schema.load(request.json)
            user = (await User.create(**data)).to_dict()
        except (ValidationError, DataError) as e:
            abort(400, message=e)

        return sanic_json(user, 201)


class UserView(HTTPMethodView):
    # noinspection PyMethodMayBeStatic
    async def get(self, _, pk: int):
        """ Get user by id. """
        user = await User.get_or_404(pk)
        return sanic_json(user.to_dict(), 200)

    # noinspection PyMethodMayBeStatic
    async def put(self, request, pk: int):
        """ Edit user. """
        user = await User.get_or_404(pk)

        try:
            data = schema.load(request.json)
            await user.update(**data).apply()

        except (ValidationError, DataError) as e:
            abort(400, message=e)

        return sanic_json(user.to_dict(), 200)

    # noinspection PyMethodMayBeStatic
    async def delete(self, _, pk: int):
        """ Delete user. """
        # Allow deleting only for the owner.
        status, user = await User.delete.where(User.id == pk).gino.status()

        return sanic_json({}, 204 if status != "DELETE 0" else 404)
