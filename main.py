from pytubefix import YouTube
from pytubefix.cli import on_progress

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=jqS4S_jxLdo"

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download()
