from settings import ma
from models.models import Event

class TodoSerializer(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "is_done")


todo_serializer = TodoSerializer()
todos_serializer = TodoSerializer(many=True)


class EventSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event


event_serializer = EventSerializer()
events_serializer = EventSerializer(many=True)
