# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base , Session

engine = create_engine('mysql://root:123456@localhost/EmpData?charset=utf8&use_unicode=0', pool_recycle=3600)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
# restaurant1 = Restaurant(name="Urban Burger")
# session.add(restaurant1)
# session.commit()
#
#
# restaurant2 = Restaurant(name="Super Stir Fry")
# session.add(restaurant2)
# session.commit()
#
# restaurant3 = Restaurant(name="Super chicken Fry")
# session.add(restaurant2)
# session.commit()


sessiondb = Session(gender = "اقایان " , price = 5000 , time_duration = "۱۲-۱۳:۳۰" ,
                   date = "۲۵ خرداد" , parking = "پارکینگ"  , address = "آدرس: نارمک، میدان هلال‌احمر، خیابان گلستان، پشت مترو فدک")
session.add(sessiondb)
session.commit()


print ("added menu items!")
