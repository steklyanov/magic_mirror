from settings import api
from views.todo_views import TodoListView, TodoEditView, TodoCreateView
from views.event_views import EventListView, EventEditView, EventCreateView

# TODOS ROUTES
api.add_resource(TodoListView, '/api/v1/todo/list')
api.add_resource(TodoCreateView, '/api/v1/todo/create')
api.add_resource(TodoEditView, '/api/v1/todo/<int:todo_id>')

# EVENT ROUTES
api.add_resource(EventListView, '/api/v1/event/list')
api.add_resource(EventCreateView, '/api/v1/event/create')
api.add_resource(EventEditView, '/api/v1/event/<int:event_id>')
