import typer
import os
import requests
import uuid

app = typer.Typer(add_completion=False)


@app.command()
def ass(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=ass'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def hentai(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=hentai'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def milf(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=milf'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def oral(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=oral'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def paizuri(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=paizuri'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def ecchi(images: int = typer.Argument(1, help="Images")):

    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=ecchi'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.command()
def ero(images: int = typer.Argument(1, help="Images")):
    for i in range(images):
        url = 'https://api.waifu.im/search/?included_tags=ero'
        r = requests.get(url).json()
        image = requests.get(r["images"][0]["url"])
        open(os.path.join(os.getcwd(),
                          f'{uuid.uuid4()}.jpg'), 'wb').write(image.content)


@app.callback()
def main():
    """
    Stay a way kid, nothing to see here. (。・ω・。)
    """


if __name__ == "__main__":
    app()
