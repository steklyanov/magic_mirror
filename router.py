from settings import api
from views import TodoListView, TodoEditView, TodoCreateView

# ROUTER
api.add_resource(TodoListView, '/todo/list')
api.add_resource(TodoCreateView, '/todo/create')
api.add_resource(TodoEditView, '/todo/<int:todo_id>')
