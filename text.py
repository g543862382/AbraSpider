from db import DB
from item import UserItem

db_ = DB()
print(db_.exist('user',1))

item = UserItem(1,'disen',20)