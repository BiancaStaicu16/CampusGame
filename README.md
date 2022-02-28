# Campus Game

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/sorinburghiu2323/Conffiliate/blob/master/LICENSE.md)

## 📖 About

Campus Game (ToBeContinued)

## 🤝 Workspaces

**NOTE:** Send Apurva your trello account name and google email to add you to it.

[Trello board for tasks]()

[Shared Google drive]()

[Discord server]()

## 🛠️ Setup

First set up your python virtual environment.

```
python -m venv .venv
```

Then activate it with:

```
.venv\Scripts\activate.bat      # Windows
.venv\bin\activate              # Linux
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