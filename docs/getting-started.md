# Getting Started

This page describes the steps needed to get the Pacific Connect Community Database set up on your local machine for development. The
approach presented here is the simplest approach, an alternative approach is briefly mentioned under [Alternative
Approach: Pyenv](#alternative-approach-pyenv) at the end.

It assumes that you have already cloned this repository to your own computer (as outlined in the `README.md` file) and
that you have a recent version of Python installed on your local computer.

Python installation instructions for several operating systems can be found at
http://pacific-coding.commoncode.io/getting-started/py-install/ - although you should install version 3.10 if possible


## Requirements

- A Git client (such as GitHub Desktop)
- This repository _cloned_ or your local computer.
- Python 3.8 or later installed

## Setup Steps

To carry out these steps, you will need to be using your computer's _command line_. If you are not familiar with the
concept of the command line an introduction can be found at
http://pacific-coding.commoncode.io/getting-started/terminal/

On the command line, you will need to be in the base directory of this repository on your computer - that is, the
directory that has the `README.md` file in it.

### 1. Create and activate a virtual environment

A _virtual environment_ (or _virtualenv_) in Python keeps the different _libraries_ you install separate for different
projects. That means that if you're working on two different projects, they can have different versions of the same
library (e.g. Django) without affecting each other.

Create the virtual environment for this project:

If using Windows:
```powershell
python -m venv venv
```

If using MacOS or Linux:
```bash
python3 -m venv venv
```

Once you have created your virtual environment, you need to _activate_ it so that Python knows to use the libraries in
your virtual environment.

To activate your virtual environment:

If using Windows:
```powershell
venv\Scripts\activate
```

If using MacOS or Linux:
```
source venv/bin/activate
```

If your virtual environment has been activated, you should see the prefix `(venv)` before the prompt on the command
line.

**NOTE: You will need to activate your virtual environment every time you want to work on this project**.

For more information about virtual environments, see:
- [Why do we need to use virtualenvs](http://pacific-coding.commoncode.io/python-intro/virtualenvs/)
- [Create a Virtual Environment](http://pacific-coding.commoncode.io/python-intro/create-a-venv/)

 
### 2. Install the Python requirements

This project has a `requirements.txt` file that lists all the Python libraries required to run the project. Once you
have activated your virtual environment, you can install the python libraries with:

```bash
pip install -r requirements.txt
```

This will install all requirements listed in the `requirements.txt` file, and as new requirements are added to the
project they will be added to the `requirements.txt` file.


### 3. Run migrations

Migrations are the way that Django manages changes to the structure of the database over time.

Before running migrations, you will need to change to the directory (`src`) that contains the code. Different projects
have different conventions about the name of the directory where the code is kept, but `src` is a common name.

```bash
cd src
```

To set up your database the first time, run:

Windows:
```bash
python manage.py migrate
```

MacOS or Linux:
```bash
python3 manage.py migrate
```

The first time you run this, you will see a series of messages that look like:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  ...
```

This indicates that the migrations have run and the database is set up.

**NOTE: You will need to run migrations fairly regularly in order to keep your database structure up to date**

A summary about database set-up in Django can be found at:
- [Pacific Coding: Set up a
  Database](http://pacific-coding.commoncode.io/django/your-first-django-project/#set-up-a-database)

More information in Migrations can be found at:
- [Django's Migrations documentation](https://docs.djangoproject.com/en/4.0/topics/migrations/)

More information on Models can be found at:
- [MDN's Django Tutorial Part 3](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- [Django's Models documentation](https://docs.djangoproject.com/en/4.0/topics/db/models/)


### 4. Continue to _Running the Application_

Now that you have installed all the prerequisites and run migrations for the first time, you can move to
[running-the-application].

## Alternative Approach: Pyenv

This approach is only recommended if you need to run multiple different versions of Python (such as Python 3.8 _and_
Python 3.10) on the same computer.

[Pyenv](https://github.com/pyenv/pyenv) is a tool that allows you to have multiple Python versions installed and switch
between them. When combined with [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) it also provides the
ability to easily switch between named virtual environments.

To install, see the instructions at [Pyenv Installation](https://github.com/pyenv/pyenv#installation) and
[Pyenv-virtualenv Installation](https://github.com/pyenv/pyenv-virtualenv#installation)



[running-the-application]: running-the-application.md