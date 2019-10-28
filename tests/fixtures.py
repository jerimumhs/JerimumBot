from pytest import fixture
from mongoengine import connect, connection


@fixture(scope='function')
def mongo(request):
    connection.disconnect_all()
    db = connect('testdb', host='mongomock://localhost')
    yield db
    db.drop_database('testdb')
    db.close()
