import datetime

import pendulum
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
    _datetime = DateTimeField(default=pendulum.now)
    _value = StringField(max_length=1, choices=CHOICES.keys(), required=True)

    meta = {
        'ordering': ['_datetime']
    }

    def __str__(self):
        return f'{self.datetime}: {self.value}'

    @property
    def datetime(self):
        return pendulum.instance(self._datetime).in_tz('America/Sao_Paulo')

    @property
    def value(self):
        return self.CHOICES.get(self._value).get('name')

    @value.setter
    def value(self, key):
        if key not in self.CHOICES.keys():
            raise ValueError(f'O valor deve estar entre {self.CHOICES.keys()}')
        self._value = key

    @property
    def sticker(self):
        return self.CHOICES.get(self._value).get('sticker')

    @classmethod
    def now(cls):
        return cls.objects.order_by('-_datetime').first()
