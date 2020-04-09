from settings import app, db
from router import *
from models import Todo
from serializer import *
db.create_all()
db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
