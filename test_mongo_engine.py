from mongoengine import *
import soshy

mk_users = soshy.genBasicUsers(100, True)

connect('test')


class User(Document):
    name = StringField(required=True)
    email = StringField(max_length=100)
    gender = StringField(max_length=6)
    password = StringField()


# *** Example of using mock for populating databases

for mk_user in mk_users:
    newUser = User(email=mk_user.email, name=mk_user.username, gender=mk_user.gender, password=mk_user.password)
    newUser.save()

for user in User.objects:
    print("Mongo User:", user.name, user.email, user.gender)
