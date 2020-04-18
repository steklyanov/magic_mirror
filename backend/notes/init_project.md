Init virtualenv

    python3 -m venv venv

Install packages

    pip install Flask Flask-SQLAlchemy, flask-migrate
    pip install flask-marshmallow marshmallow-sqlalchemy

Create initial migration

    flask db init
    flask db migrate -m "Initial migration."


Create file
* app.py
* settings.py


