import pytest


@pytest.fixture
def watch():
    from ..modules import watch
    yield watch
