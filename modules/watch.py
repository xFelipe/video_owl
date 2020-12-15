import re

VIDEO_REGEX = r'(.*)youtube.com/(.*)[&|?]v=(?P<video>[^&]*)(.*)'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'


def main():
    ...
    # https://www.youtube.com/playlist?list=PL_Q15fKxrBb5pckIW2RHwZbgf-FwRiCWr


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

if '__main__' == __name__:
    main()
