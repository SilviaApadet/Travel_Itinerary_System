from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

#Create a base class
Base= declarative_base()
# Define the database connection
DATABASE_URL = "sqlite:///travel_itinerary.db"
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)

#Define the Travel model
class User(Base):
     __tablename__='users'
     id=Column(Integer, primary_key=True)
     name=Column(String(100),nullable=False)
     email=Column(String(100),nullable=True)
     phone_number=Column(String(15),unique=True)
     current_location = Column(String, nullable=True)
     trips = relationship("Trip", back_populates="user")

     def __repr__(self):
          return f"<User(id={self.id},name='{self.name}',email='{self.email}')>"
     
class Trip(Base):
     __tablename__= 'trips'

     id= Column(Integer,primary_key=True)
     name=Column(String, nullable=False)
     user_id= Column(Integer, ForeignKey('users.id'))

     user= relationship("User", back_populates="trips")
     destinations= relationship("Destination", back_populates="trip")
     expenses= relationship("Expense", back_populates="trip")

     def __repr__(self):
          return f"<Trip(id={self.id},name='{self.name}',user_id={self.user_id})>"
class Destination(Base):
     
    __tablename__ = 'destinations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    trip = relationship("Trip", back_populates="destinations")
    activities = relationship("Activity", back_populates="destination")

    def __repr__(self):
         return f"<Destination(id={self.id},name='{self.name}',trip_id={self.trip_id})>"

class Activity(Base):
     
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    destination = relationship("Destination", back_populates="activities")

    def __repr__(self):
         return f"<Activity(id={self.id},name='{self.name}',destination_id={self.destination_id})>"
    
class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    trip = relationship("Trip", back_populates="expenses")

    def __repr__(self):
         return f"<Expense(id={self.id},amount={self.amount},category='{self.category}',trip_id={self.trip_id})>"
    # Create all tables in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)