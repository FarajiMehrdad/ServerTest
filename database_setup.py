from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String , Boolean , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer , primary_key=True)
#     name = Column(String(150) , nullable=False)
#
#
# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer , primary_key=True)
#     city = Column(String(250),nullable=False)
#
#
#
# class Facilities(Base):
#     __tablename__ = 'facilities'
#
#     parking = Column(Boolean , nullable=True)
#     dressing = Column(Boolean , nullable=True)
#     bath = Column(Boolean , nullable=True)
#
#
#
#
#
# class Venue(Base):
#     __tablename__ = 'venue'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250) , nullable=False)
#     owner = Column(Integer , ForeignKey('user.id'))
#     address = Column(Integer , ForeignKey('address.id'))
#     rate = Column(Float)
#     description = Column(String(350))



class Session(Base):
    __tablename__ = 'session'

    id = Column(Integer , primary_key=True)
    gender = Column(String(25))
   # venue = Column(Integer , ForeignKey('venue.id'))
    price = Column(Integer,nullable=False)
    time_duration = Column(String(150) , nullable=False)
    date = Column(String(150))
    salon_name = (String(150))
    parking = Column(String(150))
    footbal = Column(Boolean)
    footsal = Column(Boolean)
    address = Column(String(250))




class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


engine = create_engine('mysql://root:123456@localhost/EmpData?charset=utf8mb4&use_unicode=0', pool_recycle=3600)
Base.metadata.create_all(engine)