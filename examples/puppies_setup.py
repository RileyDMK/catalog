import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(200))
    city = Column(String(200))
    state = Column(String(20))
    zipCode = Column(Integer)
    website = Column(String(200))
    id = Column(Integer, primary_key=True)


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    dob = Column(Date)
    gender = Column(String(1))
    weight = Column(Integer)
    shelther_id = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String)
    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
