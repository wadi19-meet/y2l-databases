from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,grade,mark,section):
	product_object = Product(
		name = name,
		grade = grade,
		mark = mark,
		section = section)
	session.add(product_object)
	session.commit()

create_product("wadi", 11,97,"science")	
create_product("wada", 12,87,"science")
def update_product(name,grade):
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	product_object.grade=grade

#update_product("wada",77)

def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()

#delete_product("wadi") 

def get_product(id):
  pass
