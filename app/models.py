from app.database import Base, db_session
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# https://marshmallow-sqlalchemy.readthedocs.io/en/latest/

class Video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    code = Column(String(30), unique=True)
    playlist_id = Column(Integer, ForeignKey('playlist.id'))
    playlist = relationship('Playlist', back_populates='videos')

    def __init__(self, code, name=''):
        self.code = code
        self.name = name

    def __repr__(self):
        return f'Video {self.name}'

    def save(self):
        db_session.add(self)
        db_session.commit()


class Playlist(Base):
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-one
    __tablename__ = 'playplist'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    code = Column(String(30), unique=True)
    videos = relationship('Video', back_populates='playlist')

    def __init__(self, code, name=''):
        self.code = code
        self.name = name

    def __repr__(self):
        return f'Video {self.name}'

    def save(self):
        db_session.add(self)
        db_session.commit()


if '__main__' == __name__:
    video = Video('Test video', 'asdasd')
    print(video.code)
    video.save()
