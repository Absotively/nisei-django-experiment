This is my very rough, very incomplete experiment in making a multilingual django site that has a blog and doesn't require database schema changes to add support for a new language.

1. Make sure you have Python 3. And git, I guess.

2. Make a virtual environment and enter it.

    python3 -m venv somedirectory
    cd somedirectory

Then activate it. On bash:
    source bin/activate
  
Or on Windows, in cmd.exe:
    .\Scripts\activate.bat

See [the documentation](https://docs.python.org/3/library/venv.html) for other shells.

3. Clone the repo and enter the repo directory.

    git clone https://github.com/Absotively/nisei-django-experiment.git nisei
    cd nisei

4. Get the dependencies.

    pip install -r requirements.txt
  
5. Create the SQLite db and create an admin user.

    ./manage.py migrate
    ./manage.py createsuperuser

6. Start the dev server.

    ./manage.py runserver

Note that because this is a very rough experiment, there's nothing at the root url. Go to /admin to make a post, then /article/[slug] to see it.
