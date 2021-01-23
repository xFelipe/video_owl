from os import path

def test_db_connection(database):
    assert not path.exists(database.DB_PATH),\
        "Connection to the database incorrectly recognized."
    database.init_db()
    assert path.exists(database.DB_PATH), \
        "Connection to the database has not been established."

def test_video_table(database, models):
    database.init_db()
    assert len(models.Video.query.all()) == 0, \
        "Test saving video already started with a video in the DB."
    new_video = models.Video('codigo', 'nome')
    new_video.save()
    saved_videos = models.Video.query.all()
    assert new_video in saved_videos, \
        "Error saving or retrieving video."
