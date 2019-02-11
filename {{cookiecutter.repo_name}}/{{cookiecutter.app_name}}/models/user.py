from {{cookiecutter.app_name}}.models import DATABASE


class User(DATABASE.Model):
    __tablename__ = 'users'

    id = DATABASE.Column(DATABASE.BigInteger(), primary_key=True)
    name = DATABASE.Column(DATABASE.Unicode())
