""" Add Example app in to Tray """
import pystray
from PIL import Image


def setup(icon):
    """ Setup icon visible """
    icon.visible = True


def main():
    """ Create icon """
    width = 48
    height = 48
    color1 = '#fff'
    icon = pystray.Icon('my icon')
    image = Image.new('RGB', (width, height), color1)
    icon.icon = image
    icon.run(setup)


if __name__ == '__main__':
    main()
