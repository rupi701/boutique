from sqlalchemy import Column, Integer, String, Float
from database.database import Base

class Dress(Base):
    __tablename__ = "dresses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gender = Column(String, nullable=True)
    type = Column(String)
    quantity = Column(Integer)