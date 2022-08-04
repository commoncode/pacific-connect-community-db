# Running the Application

Once you have completed the set-up of the development environment from the [Getting Started][getting-started] page, you
can start and use the application on your local computer.

This page assumes that you are on the _command line_, in the directory containing the `README.md` file for this project.
For more information about the command line, see the [Getting Started][getting-started] page.

If you have just come from the Getting Started documentation, you may be in the `src` directory. To move out of this directory, on the command line do:

```bash
cd ..
```

That command will move you 'up' a directory, out of the `src` directory.

### 1. Activate your virtual environment

If your Python virtual environment is not already activated, activate it:

If using Windows:
```powershell
venv\Scripts\activate
```

If using MacOS or Linux:
```
source venv/bin/activate
```

You will need to do this every time you are working with this project on the command line.


### 2. Run migrations

In _Getting Started_ you will have run migrations for the first time. It is a good practice to run migrations every
time you _pull_ changes from the GitHub repository in case those changes included database migrations.

First, move back into the `src` directory:

```bash
cd src
```

Then run the migrations with:

Windows:
```bash
python manage.py migrate
```

MacOS or Linux:
```bash
python3 manage.py migrate
```
If there are no database changes, you will see a message like:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

Otherwise, if there have been database changes you will see a list of applied migrations, like:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
```

More information in Migrations can be found at:
- [Django's Migrations documentation](https://docs.djangoproject.com/en/4.0/topics/migrations/)

More information on Models can be found at:
- [MDN's Django Tutorial Part 3](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- [Django's Models documentation](https://docs.djangoproject.com/en/4.0/topics/db/models/)


### 3. Run the development server

Django incorporates its own development web server. This gives you a way to interact with the application without
needing a server on the Internet running it. In this mode, it will also present you with more detailed error messages.

To start the development server, run:

```bash
python manage.py runserver
```

Once the server has started running, you can open it in your browser (Firefox, Chroma, Safari, Edge, or whatever you
use) by going to this address:
```
http://127.0.0.1:8000/
```

You should now see the ICDP Online Directory application in your web browser.


[getting-started]: getting-started.md