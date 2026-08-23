from sqlalchemy import String, Integer, Column, Text
from database import Base


class Students(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index= True)
    name = Column(String)
    email = Column(String)
    grade = Column(String)

