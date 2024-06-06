# Hospital Inventory Management System

## Overview
This application is designed to manage a hospital's inventory, including patients, doctors, and appointments. The system provides a CLI interface for managing and viewing information.

## Features
- Manage Patients
- Manage Doctors
- Manage Appointments
- View Departments, Doctors, Patient Residents, and Patient Details
- Manage Users
- Search Patients
- Generate Reports

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/hospital-system-cli.git
    ```
2. Change into the project directory:
    ```bash
    cd hospital-system-cli
    ```
3. Install dependencies:
    ```bash
    pipenv install
    ```
4. Activate the virtual environment:
    ```bash
    pipenv shell
    ```
5. Initialize the database:
    ```bash
    python lib/init_db.py
    ```

## Usage
Run the main application:
```bash
python cli.py
```

Follow the on-screen instructions to navigate through the menus and manage the hospital inventory.

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

