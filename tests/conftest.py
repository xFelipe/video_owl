import pytest
import os

@pytest.fixture
def watch():
    from ..app import watch
    watch.DOWNLOAD_FOLDER = os.path.join('.', 'temp_downloads')
    delete_downloads(watch)
    yield watch
    delete_downloads(watch)

@pytest.fixture
def database():
    from app import database
    delete_db(database)
    yield database
    database.db_session.rollback()
    delete_db(database)

@pytest.fixture
def models():
    from app import models
    yield models

def delete_downloads(watch):
    if os.path.exists(watch.DOWNLOAD_FOLDER):
        for tmp_file_name in os.listdir(watch.DOWNLOAD_FOLDER):
            tmp_file_path = os.path.join(watch.DOWNLOAD_FOLDER, tmp_file_name)
            os.remove(tmp_file_path)
        os.rmdir(watch.DOWNLOAD_FOLDER)

def delete_db(database):
    if os.path.isfile(database.DB_PATH):
        os.remove(database.DB_PATH)
