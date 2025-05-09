import click
from pytubefix import YouTube
from pytubefix.cli import on_progress

@click.command()
@click.argument('url')
def download_video_by_link(url: str) -> None:
    """Download Youtube video via url"""
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download()

if __name__ == '__main__':
    download_video_by_link()