from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import soshy

engine = create_engine('sqlite:///test.sqlite', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    gender = Column(String)

    def __repr__(self):
        return "<User(username='{}', email='{}', gender='{}' password='{}')>".format(self.username, self.email,
                                                                                     self.gender, self.password)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# *** Creating a Test Database of 100 Mock Users: ***

mk_users = soshy.genBasicUsers(100)
user_list = []

# loop through the code, creating a list of SqlAlchemy Users using MockUsers data:
for mk_user in mk_users:
    new_user = User(username=mk_user.username, email=mk_user.email, gender=mk_user.gender, password=mk_user.password)
    user_list.append(new_user)

session.add_all(user_list)
session.commit()
