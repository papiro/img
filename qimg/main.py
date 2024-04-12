import click
from os import path
# from argparse import ArgumentParser
from PIL import Image
from io import BytesIO
# import pillow_avif

# __dirname = path.dirname(path.abspath(__file__))

@click.group()
def cli():
    pass

img_bytes = BytesIO()
img_bytes_resized = BytesIO()

@click.command()
@click.argument('filename')
def to_webp(filename):
    img = Image.open(filename)
    img.save(img_bytes, 'JPEG', quality='keep')
    img.save(img_bytes_resized, 'WEBP')

    print(f"Original {img.size}:", img_bytes.tell(), "\n")
    print(f"New {img.size}:", img_bytes_resized.tell(), "\n")

    filename, _ = path.splitext(filename)
    finished_filename = path.join(f'{filename}.webp')
    img.save(finished_filename, 'WEBP')

    img.close()

cli.add_command(to_webp)

# if __name__ == '__main__':
#     cli()
# resize preserving aspect ratio
# exif is stripped here
# img.thumbnail((650, 9999999))

# convert from RGB to P
# img = img.quantize(128)
# img = img.convert("L")
