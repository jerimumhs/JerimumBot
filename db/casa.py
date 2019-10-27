import datetime

from mongoengine import Document, DateTimeField, StringField


class Status(Document):
    CHOICES = {
        'a': {
            'name': 'Aberta',
            'sticker': 'CAADAQADXwADHaeSHfBrZMzXjtwlFgQ'
        },
        'f': {
            'name': 'Fechada',
            'sticker': 'CAADAQADYAADHaeSHb7fujge5DRfFgQ'
        }
    }

    user = StringField(required=True)
    _datetime = DateTimeField(default=datetime.datetime.utcnow)
    _value = StringField(max_length=1, choices=CHOICES.keys(), required=True)
