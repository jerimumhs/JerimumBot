from decouple import config
from mongoengine import *

from db.house import Status


connect(
    db=config('DB_NAME'),
    username=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
    port=config('DB_PORT', cast=int),
    authentication_source='admin'
)
