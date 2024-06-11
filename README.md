# Hospital Inventory Management System

## Overview
The Hospital Inventory Management System is a command-line interface (CLI) application designed to help hospitals manage their inventory efficiently. This application allows users to manage and view information related to patients, doctors, and appointments. It also provides functionalities to manage users, search patients, and generate reports.

## Features
Admin Side
.Manage Patients: Add, delete, and update patient information.

.Manage Doctors: Add, delete, and update doctor information.

.Manage Appointments: Book, update, and cancel appointments.

.Manage Users: Add and manage user accounts.

.Generate Reports: Create reports based on the hospital's data.

User Side
.View Departments: Display a list of available hospital departments.

.View Doctors: Display a list of available doctors.

.View Patient Residents: Display a list of all patient residents.

.View Patient Details: Display detailed information of a specific patient.

.View Doctor's Appointments: Check available appointments for doctors.

.Search Patients: Search for patients by different attributes.

## Installation
Prerequisites

.Python 3.x

.Pipenv

Steps

Clone the repository:

git clone <https://github.com/your-username/hospital-system-cli.git>

Change into the project directory:

cd hospital-system-cli

Install dependencies:

pipenv install

Activate the virtual environment:

pipenv shell

Initialize the database:

python lib/init_db.py

## Usage
To run the main application, execute the following command:
python lib/cli.py

## Development
For development purposes, you can use `ipython` for an interactive shell.

### Database Initialization
To reset the database, run:
```bash
python lib/init_db.py
```


## Dependencies
- Python 3.x
- SQLAlchemy

## License
This project is licensed under the MIT License.

