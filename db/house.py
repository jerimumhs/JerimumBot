import pendulum
from mongoengine import Document, DateTimeField, StringField, IntField


class Status(Document):
    FECHADA = 'f'
    ABERTA = 'a'
    CHOICES = {
        ABERTA: {
            'name': 'Aberta',
            'sticker': 'CAADAQADXwADHaeSHfBrZMzXjtwlFgQ'
        },
        FECHADA: {
            'name': 'Fechada',
            'sticker': 'CAADAQADYAADHaeSHb7fujge5DRfFgQ'
        }
    }

    user = IntField(required=True)
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

    @classmethod
    def create(cls, user, value):
        instance = cls(user=user, _value=value)
        instance.save()
        return instance

    @classmethod
    def aberta(cls, user):
        instance = cls.create(user=user, value=cls.ABERTA)
        return instance

    @classmethod
    def fechada(cls, user):
        instance = cls.create(user=user, value=cls.FECHADA)
        return instance
