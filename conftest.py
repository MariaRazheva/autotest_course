import pytest
import datetime

@pytest.fixture(scope = 'function')
def lead_time():
    begin = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print('\n', end - begin)


@pytest.fixture(autouse=True, scope = 'class')
def begin_end_time():
    print('\n', datetime.datetime.now())
    yield
    print('\n', datetime.datetime.now())