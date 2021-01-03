from os import path

def test_db_connection(database):
    assert not path.exists(database.DB_PATH),\
        "Connection to the database incorrectly recognized."
    database.init_db()
    assert path.exists(database.DB_PATH), \
        "Connection to the database has not been established."
