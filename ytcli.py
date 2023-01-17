import click
from pytube import YouTube, exceptions


@click.group()
def ytcli():
    """
    ytcli is command line interface for YouTube
    """
    pass


@click.group(name="download")
def download_group():
    """
    This group is for download operations
    """
    pass


@click.command(name="video")
@click.argument("url")
def download_video(url: str):
    """
    This command is for downloading video
    """
    youtube_object = YouTube(url)
    video = youtube_object.streams.get_highest_resolution()
    video.download()
    print("Download is completed successfully")


ytcli.add_command(download_group)
download_group.add_command(download_video)
