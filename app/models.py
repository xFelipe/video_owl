from app.database import Base, db_session, init_db
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship


# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many

video_in_playlist = Table('video_in_playlist', Base.metadata,
    Column('video_id', Integer, ForeignKey('video.id')),
    Column('playlist_id', Integer, ForeignKey('playlist.id')),
    extend_existing=True
)

class Video(Base):
    __tablename__ = 'video'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    code = Column(String(30), unique=True)
    playlists = relationship('Playlist',
                             secondary=video_in_playlist,
                             backref='videos')

    def __init__(self, code, name=''):
        self.code = code
        self.name = name

    def __repr__(self):
        return f'Video {self.name}'

    def save(self):
        db_session.add(self)
        db_session.commit()


class Playlist(Base):
    __tablename__ = 'playlist'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    code = Column(String(30), unique=True)

    def __init__(self, code, name=''):
        self.code = code
        self.name = name

    def __repr__(self):
        return f'Playlist {self.name}'

    def save(self):
        db_session.add(self)
        db_session.commit()


if '__main__' == __name__:
    # video = Video('CodigoTeste5', 'video5')
    # video.save()
    for v in Video.query.all():
        print(f'Nome: {v.name} - Código: {v.code}')
