# Travel_Itinerary_System
📌 Project Overview
The Travel_Itinerary_System is a command-line application that allows users to:

Add and delete user to the system
Add destinations in the system
Add and delete trips in the system
Add activities in the system
List trips
Calculate trip expense

Built using Python, SQLAlchemy, SQLite, and Click, this CLI-based app helps users efficiently track their movie-watching experience.

🚀 Features
✅ User Management – Add and list users.
✅ Trip Management – Add, list, and delete trips.
✅ Activity Management – Add activities.
✅ Trip Expense – Calculate trip expense.

🛠 Technologies Used
Python 3
SQLAlchemy ORM
SQLite (Database)
Click (Command-line interface)
Alembic (Database migrations)
🔧 Installation & Setup
Clone the repository:
git clone git@github.com:SilviaApadet/Travel_Itinerary_System.git
cd Travel_Itinerary_System
Set up a virtual environment:
python -m venv env
source env/bin/activate  
Install dependencies:
pip install -r requirements.txt
Run database migrations:
alembic upgrade head
🎯 Usage
Run the CLI tool using:

python main.py
You'll be presented with a menu, where you can choose actions like adding user, addding activities, and calculating trip expense.

📜 CLI Commands
1️⃣ Add a User
python main.py add-user
2️⃣ Add a trip
python main.py add-trips
3️⃣ List trips
python main.py list-trips

📌 Database Schema
User (id, name, email,phone_number)
Trip (id, name, genre, user_id)
Destination (id, name, trip_id)
Activities (id, name, destination_id)
🛠 Future Enhancements
🚀 Add authentication for users.
🚀 Improve recommendation algorithm.
🚀 Implement a web interface.

📄 License
This project is licensed under the MIT License.

💡 Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or want to suggest an enhancement.

