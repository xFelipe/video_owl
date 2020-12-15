
def test_load_url_video(watch):
    load_data = watch.load_url("https://www.youtube.com/watch?v=MKgR8M2B5P8")
    assert load_data.get("video") == "MKgR8M2B5P8",\
        "The video code was not loaded correctly"

def test_load_url_playlist(watch):
    load_data = watch.load_url("https://www.youtube.com/watch?v=ni8S1ZTvVEc&list=PL991DC6D796E904D1&ab_channel=antuycuyen")
    assert load_data.get("playlist") == "PL991DC6D796E904D1",\
        "The playlist code was not loaded correctly"


"""
OR
{
    "playlist": "MKgR8M2B5P8"
}
"""
