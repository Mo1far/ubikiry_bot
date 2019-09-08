from peewee import *

db = SqliteDatabase('users.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)
    ref = IntegerField(default=0)
    username = CharField(null=True)
    first_name = CharField()
    last_name = CharField
    referral_list = TextField()

    @classmethod
    def get_user(cls, user_id):
        return cls.get(user_id=user_id)

    @classmethod
    def get_ref_count(cls, user_id):
        u = cls.get_user(user_id)
        return u.ref

    @classmethod
    def increase_ref_count(cls, user_id, referral_id):
        user = cls.get_user(user_id)
        user.referral_list += f"{referral_id}, "
        user.ref += 1
        user.save()

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    @classmethod
    def create_user(cls, user_id, username, first_name, last_name):
        user, created = cls.get_or_create(user_id=user_id, username=username, first_name=first_name, last_name=last_name, referral_list='')

# создаём таблицы, запустить 1 раз и закомментировать
# db.create_tables([Users])