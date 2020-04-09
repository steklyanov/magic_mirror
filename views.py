from flask_restful import Resource, reqparse
from models import Todo
from settings import db
from serializer import todo_serializer, todos_serializer

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Specify the name of the TODO')
parser.add_argument('is_done', type=bool, help='Specify current status of TODO')


class TodoListView(Resource):
    def get(self):
        todos = Todo.query.all()
        print(todos)
        return todos_serializer.dump(todos), 200


class TodoEditView(Resource):
    def get(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        return todo_serializer.dump(todo), 200

    def put(self, todo_id):
        args = parser.parse_args()
        todo = Todo.query.filter_by(id=todo_id).first().update(args)
        return todo_serializer.dump(todo), 200

    def delete(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        return 204


class TodoCreateView(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        todo = Todo(name=args['name'])
        db.session.add(todo)
        db.session.commit()
        return todo_serializer.dump(todo), 201
