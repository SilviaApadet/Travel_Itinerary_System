import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from models import Base, User, Trip, Destination, Activity, Expense

#  SQLite Database URL
engine = create_engine('sqlite:///travel_itinerary.db')

#  Create Tables if Not Exists
Base.metadata.create_all(engine)

#  Create a new database session
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Travel Itinerary CLI"""
    pass

#  Add User
@click.command()
@click.argument('name')
def add_user(name):
    """Add a new user"""
    user = User(name=name)
    session.add(user)
    session.commit()
    click.echo(f"User '{name}' added successfully!")

#  List Users
@click.command()
def list_users():
    """List all users"""
    users = session.query(User).all()
    if not users:
        click.echo("No users found!")
        return
    for user in users:
        click.echo(f"ID: {user.id}, Name: {user.name}")

# Add Destination
def add_destination_to_trip(trip):
    """Adds a destination to a trip."""
    destination_name = input("Enter destination name: ")
    destination = Destination(name=destination_name, trip_id=trip.id)
    session.add(destination)
    session.commit()
    print(f"Destination '{destination_name}' added to trip '{trip.name}'!\n")

    # Click command version of add_destination
@click.command()
@click.argument('name')
def add_destination(name):
    """Add a new destination"""
    destination = Destination(name=name)
    session.add(destination)
    session.commit()
    click.echo(f"Destination '{name}' added successfully!")


# ✅ Add Activity
@click.command()
@click.argument('name')
@click.argument('destination_id', type=int)
@click.argument('cost', type=float)
def add_activity(name, destination_id, cost):
    """Add a new activity to a destination"""
    destination = session.query(Destination).filter_by(id=destination_id).first()
    if not destination:
        click.echo("Destination not found!")
        return
    activity = Activity(name=name, destination_id=destination_id, cost=cost)
    session.add(activity)
    session.commit()
    click.echo(f"Activity '{name}' added to Destination ID {destination_id}.")

# ✅ List All Trips
@click.command()
def list_trips():
    """List all trips"""
    trips = session.query(Trip).all()
    if not trips:
        click.echo("No trips found!")
        return
    for trip in trips:
        click.echo(f"Trip ID: {trip.id}, User ID: {trip.user_id}, Destination ID: {trip.destination_id}")
# ✅ Delete a Trip
@click.command()
@click.argument('trip_id', type=int)
def delete_trip(trip_id):
    """Delete a trip"""
    trip = session.query(Trip).filter_by(id=trip_id).first()
    if not trip:
        click.echo("Trip not found!")
        return

    session.delete(trip)
    session.commit()
    click.echo(f"Trip ID {trip_id} deleted.")

#  Delete a User
@click.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    """Delete a user"""
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        click.echo("User not found!")
        return

    session.delete(user)
    session.commit()
    click.echo(f"User ID {user_id} deleted.")

#  Calculate Total Trip Expense
@click.command()
@click.argument('trip_id', type=int)
def calculate_trip_expense(trip_id):
    """Calculate total expense for a trip"""
    trip = session.query(Trip).filter_by(id=trip_id).first()
    if not trip:
        click.echo("Trip not found!")
        return

    total_cost = session.query(func.sum(Expense.amount)).filter_by(trip_id=trip.id).scalar() or 0
    click.echo(f"Total Expense for Trip ID {trip_id}: ${total_cost:.2f}")

#  Add Commands to CLI
cli.add_command(add_user)
cli.add_command(list_users)
cli.add_command(add_destination)
cli.add_command(add_activity)
cli.add_command(list_trips)
cli.add_command(delete_trip)
cli.add_command(delete_user)
cli.add_command(calculate_trip_expense)

#  Interactive CLI for Users
def create_user():
    """Prompts the user to create a new traveler profile."""
    name = input("Enter your name: ")
    email = input("Enter your email: ") 
    print(f"Welcome, {name}! Your email is {email}.") 
    phone_number = input("Enter your phone number (optional): ") or None

    user = User(name=name, email=email, phone_number=phone_number)  
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
    destination = Destination(name=destination_name,trip_id=trip.id)
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
    total = session.query(func.sum(Expense.amount)).filter_by(trip_id=trip.id).scalar()
    print(f"Total expenses for '{trip.name}': ${total if total else 0:.2f}\n")

def main():
    print("Welcome to the Travel Itinerary Planner!\n")
    user = create_user()

    while True:
        print("\nMenu:")
        print("1. Create a new trip")
        print("2. Add a destination to a trip")
        print("3. Add an expense")
        print("4. View total trip expenses")
        print("5. Add new user")
        print("6. List users")
        print("7. Delete existing user")
        print("8. Delete existing trips")
        print("9. List trips")
        print("10. Add activity")
        print("11. Calculate total expense")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            trip = create_trip(user)

        elif choice == "2":
            add_destination(trip)

        elif choice == "3":
            add_expense(trip)

        elif choice == "4":
            view_total_expense(trip)

        elif choice == "5":
            add_user()

        elif choice == "6":
            list_users()

        elif choice == "7":
            user_id = int(input("Enter User ID to delete: "))
            delete_user(user_id)

        elif choice == "8":
            trip_id = int(input("Enter Trip ID to delete: "))
            delete_trip(trip_id)

        elif choice == "9":
            list_trips()

        elif choice == "10":
            destination_id = int(input("Enter Destination ID: "))
            name = input("Enter activity name: ")
            cost = float(input("Enter activity cost: "))
            add_activity(name, destination_id, cost)

        elif choice == "11":
            trip_id = int(input("Enter Trip ID: "))
            calculate_trip_expense(trip_id)

        elif choice == "12":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
