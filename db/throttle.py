import pendulum
from decouple import config
from mongoengine import Document, DateTimeField, StringField


class CommandCall(Document):
    COACH = '1'
    CLIMA = '2'
    CHOICES = {
        COACH: '/coach',
        CLIMA: '/clima'
    }

    COOLDOWN = config('COMMAND_COOLDOWN', default=300, cast=int)

    user = StringField(required=True)
    _datetime = DateTimeField(default=pendulum.now)
    _value = StringField(max_length=1, choices=CHOICES.keys(), required=True)

    meta = {
        'ordering': ['_datetime']
    }

    def __str__(self):
        return f'{self.datetime}: {self.value}'

    def __eq__(self, other):
        try:
            return self.id == other.id
        except AttributeError:
            return False

    @property
    def datetime(self):
        return pendulum.instance(self._datetime).in_tz('America/Sao_Paulo')

    @property
    def value(self):
        return self.CHOICES.get(self._value)

    @value.setter
    def value(self, key):
        if key not in self.CHOICES.keys():
            raise ValueError(f'O valor deve estar entre {self.CHOICES.keys()}')
        self._value = key

    def is_cooldown_over(self):
        time_diff = pendulum.now() - self.datetime
        return time_diff.seconds >= self.COOLDOWN

    @property
    def cooldown_left(self):
        time_diff = pendulum.now() - self.datetime
        return self.COOLDOWN - time_diff.seconds

    @classmethod
    def last_command(cls):
        return cls.objects.order_by('-_datetime').first()

    @classmethod
    def last_coach(cls):
        return cls.objects(_value=cls.COACH).order_by('-_datetime').first()

    @classmethod
    def last_clima(cls):
        return cls.objects(_value=cls.CLIMA).order_by('-_datetime').first()

    @classmethod
    def create(cls, user, value):
        instance = cls(user=user, _value=value)
        instance.save()
        return instance

    @classmethod
    def coach(cls, user):
        return cls.create(user=user, value=cls.COACH)

    @classmethod
    def clima(cls, user):
        return cls.create(user=user, value=cls.CLIMA)

    @classmethod
    def allow_call(cls, command=COACH, shared=False):
        last_call = None

        if command == CommandCall.COACH:
            last_call = cls.last_coach()
        elif command == CommandCall.CLIMA:
            last_call = cls.last_clima()
        elif not shared:
            raise ValueError('Comando não identificado')

        if shared:
            last_call = cls.last_command()

        if last_call is None or last_call.is_cooldown_over():
            return True
        return False
