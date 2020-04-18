from flask_restful import Resource, reqparse
from models.models import Event
from settings import db
from serializer import todo_serializer, todos_serializer, event_serializer, events_serializer
import datetime
from sqlalchemy import and_
from flask_restful import request
from settings import db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Specify the name')
parser.add_argument('description', type=str, help='Specify description')
parser.add_argument('start_date', type=str, help='start_date %s, %r'.format(db.Date, db.Date))
parser.add_argument('start_time', type=str, help='start_time')
parser.add_argument('end_date', type=str, help='end_date')
parser.add_argument('end_time', type=str, help='end_time')
parser.add_argument('full_day', type=bool, help='full day')

def get_interval(args):
    month_start = int(args['ms'])
    year_start = int(args['ys'])
    day_start = int(args['ds'])

    month_end = int(args['me'])
    year_end = int(args['ye'])
    day_end = int(args['de'])

    start_date = datetime.date(year_start, month_start, day_start)
    end_date = datetime.date(year_end, month_end, day_end)
    return start_date, end_date


class EventListView(Resource):
    def get(self):
        args = request.args
        print(args)
        start_date, end_date = get_interval(args)
        print(start_date, end_date)
        todos = Event.query.filter(and_(Event.start_date >= start_date, Event.end_date <= end_date)).all()
        print(todos)
        return events_serializer.dump(todos), 200


class EventEditView(Resource):
    def get(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        return event_serializer.dump(event), 200

    def put(self, event_id):
        args = parser.parse_args()
        event = Event.query.filter_by(id=event_id).first().update(args)
        return event_serializer.dump(event), 200

    def delete(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        db.session.delete(event)
        return 204


class EventCreateView(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        start_time = datetime.datetime.strptime(args['start_time'], '%H:%M').time()
        end_time = datetime.datetime.strptime(args["end_time"], '%H:%M').time()
        start_date = datetime.datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        print(start_time, end_time, start_date, end_date)
        event = Event(name=args['name'], description=args['description'], start_date=start_date,
                      start_time=start_time, end_date=end_date, end_time=end_time, full_day=args['full_day'])
        db.session.add(event)
        db.session.commit()
        return event_serializer.dump(event), 201