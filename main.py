from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from models import  Base, User, Trip, Destination, Activity, Expense
import click


def main():
    #create the database engine

    engine= create_engine('sqlite:/travel_itinerary.db')
    #create the tables
    Base.metadata.create_all(engine)
    
# Create a new database session
Session = sessionmaker(bind=create_engine)
session = Session()

def create_user():
    """Prompts the user to create a new traveler profile."""
    name = input("Enter your name: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} has been created successfully!\n")
    return user

def create_trip(user):
    """Allows a user to create a trip."""
    trip_name = input("Enter trip name: ")
    trip = Trip(name=trip_name, user_id=user.id)
    session.add(trip)
    session.commit()
    print(f"Trip '{trip_name}' created successfully!\n")
    return trip

def add_destination(trip):
    """Adds a destination to a trip."""
    destination_name = input("Enter destination name: ")
    destination = Destination(name=destination_name, trip_id=trip.id)
    session.add(destination)
    session.commit()
    print(f"Destination '{destination_name}' added to trip '{trip.name}'!\n")

def add_expense(trip):
    """Records an expense for a trip."""
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Transport, Food, Hotel, etc.): ")
    expense = Expense(amount=amount, category=category, trip_id=trip.id)
    session.add(expense)
    session.commit()
    print(f"Expense of ${amount} for '{category}' added to trip '{trip.name}'!\n")

def view_total_expense(trip):
    """Calculates and displays the total expenses for a trip."""
    total = session.query(Expense).filter_by(trip_id=trip.id).sum(Expense.amount)
    print(f"Total expenses for '{trip.name}': ${total}\n")

def main():
    print("Welcome to the Travel Itinerary Planner!\n")
    user = create_user()

    while True:
        print("\nMenu:")
        print("1. Create a new trip")
        print("2. Add a destination to a trip")
        print("3. Add an expense")
        print("4. View total trip expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            trip = create_trip(user)
        elif choice == "2":
            trip_id = int(input("Enter trip ID: "))
            trip = session.query(Trip).get(trip_id)
            if trip:
                add_destination(trip)
            else:
                print("Trip not found!")
        elif choice == "3":
            trip_id = int(input("Enter trip ID: "))
            trip = session.query(Trip).get(trip_id)
            if trip:
                add_expense(trip)
            else:
                print("Trip not found!")
        elif choice == "4":
            trip_id = int(input("Enter trip ID: "))
            trip = session.query(Trip).get(trip_id)
            if trip:
                view_total_expense(trip)
            else:
                print("Trip not found!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
