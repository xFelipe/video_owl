import pytest
import os
import shutil


@pytest.fixture
def watch():
    from ..modules import watch
    if not watch.DOWNLOAD_FOLDER.endswith('temp_tests'):
        watch.DOWNLOAD_FOLDER = os.path.join('.', 'temp_downloads')
    delete_downloaded_files(watch)
    yield watch
    delete_downloaded_files(watch)


def delete_downloaded_files(watch):
    if os.path.exists(watch.DOWNLOAD_FOLDER):
        for temp_file_name in os.listdir(watch.DOWNLOAD_FOLDER):
            temp_file_path = os.path.join(watch.DOWNLOAD_FOLDER, temp_file_name)
            os.remove(temp_file_path)
        os.rmdir(watch.DOWNLOAD_FOLDER)
