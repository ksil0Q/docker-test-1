import json
from pony.orm import *
from pony import orm
import datetime

with open("general_config", "r") as config:
    db_config = json.load(config)['DATABASE']

db = Database()

db.bind(provider='postgres',
        user=db_config['USER'],
        password=db_config['PASSWORD'],
        host=db_config['HOST'],
        dbname=db_config['DB_NAME'])


class User(db.Entity):
    _table_ = 'test_users'
    id = orm.PrimaryKey(int, auto=True)
    time = orm.Optional(datetime.time)
    connection_date = orm.Required(datetime.date)


db.generate_mapping(create_tables=True)


class UserManager(object):
    @db_session
    def add_visits(self, data: dict):
        User(
            time=data['time'],
            connection_date=data['date']
        )
        return User
