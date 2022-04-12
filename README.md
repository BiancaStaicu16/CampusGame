# Campus Game

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/sorinburghiu2323/Conffiliate/blob/master/LICENSE.md)

## 📖 About

Campus Game 

ECM2434 Group 23 Software Engineering Project

Campus Game is a platform that offers students the opportunity to discover and interact with new people around the campus of University of Exeter. Play the game and scan the QR codes when you arrive at a location. Get involved and receive cards and points which go towards you final score. Team up with your friends and play it as a team.

Some feature of the Campus Game offer:

1) Ability to freely register and login.
2) Ability to scan the QR code when arriving at a location on campus.
3) Ability to earn card when scanning the QR codes.
4) Ability to interact with other people by playing the game together.
5) Ability to discover the campus while playing the game.


## 🤝 Workspaces


[Trello board for tasks](https://trello.com/b/jl8CAvTH/kanban-board-group-software-dev)

[Shared Google drive](https://drive.google.com/drive/folders/18fkR52ZooqxcOuMDD-h8JmS94_OvELeL)


## 🛠️ Setup

First set up your python virtual environment.

```
python -m venv .venv
```

Then activate it with:

```
.venv\Scripts\activate.bat      # Windows
.venv\bin\activate              # Linux
source <venv> bin/activate      # MacOS
```

Install python dependencies:
```
pip install -r requirements-base.txt
```

Do your migrations (create your development database):
```
python manage.py migrate
```

Run the django server using:
```
python manage.py runserver
```

### Next install the VueJS frontend dependencies:

```
cd frontend
npm install
```
**NOTE:** When you pull changes that others have made, you may want to do 
`npm install` again to ensure any additional dependencies have been added.

Next, install the Google Maps API Dependency 
```
npm install --save vue-geolocation-api
```

Next, install the QR Code Dependency 
```
npm install --save vue-qrcode-reader
```

Now to build the frontend, there are two ways:

Watches for any changes in the filetree and recompiles when detects a change:
```
npm run watch
npm run serve
```

Compiles and minifies for production:
```
npm run build
```

### Need some test data?

Run the bootstrap to autogenerate some dummy data using:
```
python manage.py bootstrap
```
**NOTE:** Do this after migrating for the first time.

### Having a migration error?

This may be due to a database update. Simply drop you current database and create a new one as follows:
1. Delete `db.sqlite3` file
2. Run `python manage.py migrate`
