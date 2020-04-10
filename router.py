from settings import api
from views.todo_views import TodoListView, TodoEditView, TodoCreateView
from views.event_views import EventListView, EventEditView, EventCreateView

# TODOS ROUTES
api.add_resource(TodoListView, '/todo/list')
api.add_resource(TodoCreateView, '/todo/create')
api.add_resource(TodoEditView, '/todo/<int:todo_id>')

# EVENT ROUTES
api.add_resource(EventListView, '/event/list')
api.add_resource(EventCreateView, '/event/create')
api.add_resource(EventEditView, '/event/<int:event_id>')
