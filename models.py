from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#Create a base class
Base= declarative_base()

#Define the Travel model
class User(Base):
     __tablename__='users'
     id=Column(Integer, primary_key=True)
     name=Column(String(100),nullable=False)
     email=Column(String(100),nullable=False)

     def __repr_(self):
          return f"<User(id={self.id},name='{self.name}',email='{self.email}',)"