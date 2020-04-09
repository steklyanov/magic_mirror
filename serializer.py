from settings import ma


class TodoSerializer(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "is_done")


todo_serializer = TodoSerializer()
todos_serializer = TodoSerializer(many=True)
