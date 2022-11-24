# Plan Your Week

REST API that combines two existing APIs and offers you an activity for each day of the week depending on the weather.

The data is downloaded from:
* https://weatherdbi.herokuapp.com/
* https://www.boredapi.com/


## Installation
After cloning the repository follow the steps below:

Create a new environment variable called `SECRET_KEY` and assign a value to it. The value will be your secret key.

Create a new virtual environment.
```
python -m venv myvenv
```
Run the virtual environment.
```
source /path/to/myvenv/Scripts/activate
```
Upgrade pip.
```
python -m pip install --upgrade pip
```
Install the required packages.
```
pip install -r requirements.txt
```
Run the development server.
```
python manage.py runserver
```

## Consuming the API

* Getting a new schedule for the next week:
  `GET http://127.0.0.1:8000/{city}`

* Getting the schedule from the database:
  `GET http://127.0.0.1:8000/days/list/`

* Deleting all records in database:
  `DELETE http://127.0.0.1:8000/days/list/`
  
* Adding a schedule for a day:
  `POST http://127.0.0.1:8000/days/list/new/`
  
* Getting the schedule for the day by id:
  `GET http://127.0.0.1:8000/days/list/{id}`
  
* Updating the schedule for the day by id:
  `PUT http://127.0.0.1:8000/days/list/{id}}`
  
* Deleting the schedule for the day by id:
  `DELETE http://127.0.0.1:8000/days/list/{id}}`
