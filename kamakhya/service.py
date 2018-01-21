from cgitb import strong

from kamakhya.models import *
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drawingtool.settings")
    canvas = Canvas(
        width=50,
        height=50,
        stroke="#082838",
        fill="#082898"
    )
    circle = Circle(
        r=10,
        cx=34,
        cy=65,
        stroke="#082838",
        fill="#082898"
    )
    print(circle.get_tag())
