LINK_WITH_VIDEO = 'https://www.youtube.com/watch?v=MKgR8M2B5P8'
VIDEO_CODE = 'MKgR8M2B5P8'
LINK_WITH_PLAYLIST = 'https://www.youtube.com/watch?v=ni8S1ZTvVEc&list=PL991DC6D796E904D1&ab_channel=antuycuyen'  # noqa
PLAYLIST_CODE = 'PL991DC6D796E904D1'
LINK_WITH_VIDEO_AND_PLAYLIST = 'https://www.youtube.com/watch?v=bESGLojNYSo&list=PLCB4F961F723051AC&ab_channel=LadyGagaVEVO'  # noqa
VIDEO_AND_PLAYLIST_CODES = 'bESGLojNYSo', 'PLCB4F961F723051AC'
INVALID_LINK = 'https://www.youtube.com/watch?test=ASD123&ab_channel=LadyGagaVEVO'  # noqa


def test_load_video_url(watch):
    url_info = watch.load_url(LINK_WITH_VIDEO)
    assert url_info.get('video') == VIDEO_CODE,\
        'Video code was not loaded correctly'

def test_load_playlist_url(watch):
    url_info = watch.load_url(LINK_WITH_PLAYLIST)
    assert url_info.get('playlist') == PLAYLIST_CODE,\
        'Playlist code was not loaded correctly'

def test_load_video_and_playlist_url(watch):
    url_info = watch.load_url(LINK_WITH_VIDEO_AND_PLAYLIST)
    video_code, playlist_code = VIDEO_AND_PLAYLIST_CODES
    assert url_info.get('video') == video_code, \
        'Video code was not loaded correctly'
    assert url_info.get('playlist') == playlist_code, \
        'Playlist code was not loaded correctly'

def test_not_load_video_or_url(watch):
    url_info = watch.load_url(INVALID_LINK)
    assert url_info.get('video') is None, 'Video info was loaded incorrectly'
    assert url_info.get('playlist') is None, \
        'Playlist info was loaded incorrectly'

def test_download_video(watch):
    assert not watch.video_was_downloaded(VIDEO_CODE), \
        'Video was downloaded correctly'
    watch.download_video(VIDEO_CODE)
    assert watch.video_was_downloaded(VIDEO_CODE), \
        'Video was not downloaded correctly'
