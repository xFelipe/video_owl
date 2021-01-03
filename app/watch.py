import re
import pafy
from os.path import exists, join, abspath, isdir
from os import mkdir, listdir

VIDEO_REGEX = r'(.*)youtube.com/(.*)[&|?]v=(?P<video>[^&]*)(.*)'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'
DOWNLOAD_FOLDER = abspath('downloads')


def main():
    media_data = load_url('https://www.youtube.com/watch?v=bESGLojNYSo')
    download_video(media_data.get('video'))

def load_url(url):
    """Save the playlist or video link"""
    video_match = re.match(VIDEO_REGEX, url)
    playlist_match = re.match(PLAYLIST_REGEX, url)

    video = video_match.groupdict() if video_match else None
    playlist = playlist_match.groupdict() if playlist_match else None

    urls = {}

    if video is not None:
        urls.update(video)
    if playlist is not None:
        urls.update(playlist)

    return urls

def download_video(video_code):
    if not exists(DOWNLOAD_FOLDER): mkdir(DOWNLOAD_FOLDER)
    video = pafy.new(video_code)
    video_stream = video.getbest(preftype='MP4', ftypestrict=False)
    filename = video_code + '.' + video_stream._extension
    video_stream.download(join(DOWNLOAD_FOLDER, filename))

def video_was_downloaded(video_code):
    if exists(exists(DOWNLOAD_FOLDER)) and isdir(DOWNLOAD_FOLDER):
            downloaded_videos = listdir(DOWNLOAD_FOLDER)
            return [filename for filename in downloaded_videos
                    if filename.startswith(video_code+'.')]
    return []


if '__main__' == __name__:
    main()
