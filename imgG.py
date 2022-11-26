import nsfw as nsfw
import typer
import os
import requests
import uuid

from typing import Optional

app = typer.Typer(add_completion=False)
app.add_typer(nsfw.app, name="nsfw")
__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"imgG CLI Version: {__version__}")
        raise typer.Exit()


@app.command()
def random(images: int = typer.Argument(1, help="Images"),
           width: int = typer.Argument(1920, help="Images width"),
           height: int = typer.Argument(1080, help="Images height")):
    """Random will generating random images."""
    for i in range(images):
        url = f'https://picsum.photos/{width}/{height}'
        r = requests.get(url, allow_redirects=True)
        open(os.path.join(os.getcwd(),
             f'{uuid.uuid4()}.jpg'), 'wb').write(r.content)


@app.command()
def meat(images: int = typer.Argument(1, help="Images"),
         width: int = typer.Argument(1920, help="Images width"),
         height: int = typer.Argument(1080, help="Images height")):
    """meat will generating meat images."""
    for i in range(images):
        url = f'https://baconmockup.com/{width}/{height}'
        r = requests.get(url, allow_redirects=True)
        open(os.path.join(os.getcwd(),
             f'{uuid.uuid4()}.jpg'), 'wb').write(r.content)


@app.command()
def catboy(images: int = typer.Argument(1, help="Images")):
    """
    catboy will generating anime catboy images (only 5000 images per day)
    """
    for i in range(images):
        url = 'https://api.catboys.com/img'
        r = requests.get(url).json()
        image = requests.get(r["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def neko(images: int = typer.Argument(1, help="Images")):
    """
    neko will generating anime cat girl images.
    """
    for i in range(images):
        url = 'https://nekos.best/api/v2/neko'
        r = requests.get(url).json()
        image = requests.get(r["results"][0]['url'])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def husbando(images: int = typer.Argument(1, help="Images")):
    """
    husbando will generating anime husbando images.
    """
    for i in range(images):
        url = 'https://nekos.best/api/v2/husbando'
        r = requests.get(url).json()
        image = requests.get(r["results"][0]['url'])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def waifu(images: int = typer.Argument(1, help="Images")):
    """
    waifu will generating anime waifu images.
    """
    for i in range(images):
        url = 'https://nekos.best/api/v2/waifu'
        r = requests.get(url).json()
        image = requests.get(r["results"][0]['url'])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def kitsune(images: int = typer.Argument(1, help="Images")):
    """
    kitsune will generating anime kitsune images.
    """
    for i in range(images):
        url = 'https://nekos.best/api/v2/kitsune'
        r = requests.get(url).json()
        image = requests.get(r["results"][0]['url'])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "-v", "--version", help="print version number and exit", callback=version_callback
    ),
):
    """
    imgG or Image Genterator is a Tool for generating images from opensource API     
    """


if __name__ == "__main__":
    app()
