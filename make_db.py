# -- to drop the database in python3---
from main import db
db.drop_all()
db.create_all()
print("Created db", db)