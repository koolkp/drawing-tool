# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from kamakhya.models import *


def index(request):
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

    line = Line(
        x1=10,
        x2=34,
        y1=65,
        y2=23,
        fill="#082898"
    )

    rect = Rectangle(
        x=10,
        y=65,
        width=19,
        height=20,
        fill="#082898"
    )

    objects = [circle, line, rect]
    tags = canvas.get_header()
    for object in objects:
        if object.fill is None:
            object.fill = canvas.fill
        if object.stroke is None:
            object.stroke = canvas.stroke
        tags += object.get_tag()
    tags += canvas.get_footer()
    print(tags)
    return HttpResponse(str(tags))


def getHW(d):
    hh = d.split()
    h = hh[0]
    w = hh[1]
    return h, w


def getCo(d):
    hh = d.split("coordinate")
    return getHW(hh[1])


def setCircle(x, y, r, f, s):
    circle = Circle(
        r=r,
        cx=x,
        cy=y,
        stroke=s,
        fill=f
    )
    return circle


def setLine(x1, y1, x2, y2, f, s):
    line = Line(
        x1=x1,
        x2=x2,
        y1=y1,
        y2=y2,
        fill=f,
        stroke=s
    )
    return line


def setRect(x, y, w, h, f, s):
    rect = Rectangle(
        x=x,
        y=y,
        width=w,
        height=h,
        fill=f,
        stroke=s
    )
    return rect


# def setCircle(x,y,r,f,s):
#     circle = Circle(
#         r=r,
#         cx=x,
#         cy=y,
#         stroke=s,
#         fill=f
#     )
#     return circle

def getR(x, y, x1, y1):
    x = int(x)-int(x1)
    y = int(y)-int(y1)
    return str(int(x**2 + y**2)**(1/2))
    # return 10

@csrf_exempt
def parse(request):
    data = request.POST.get("parse")
    d = data.split('\n')
    objects = []
    object = None
    h, w = getHW(d[0])
    hh = d[1].split("setFillColor")
    fill = hh[1]
    hh = d[2].split("setStrokeColor")
    stroke = hh[1]
    i = 3
    canvas = Canvas(
        width=w,
        height=h,
        stroke=stroke,
        fill=fill
    )
    try:
        while True:
            hh = d[i].split()
            i += 1
            if len(hh) == 1:
                object = hh[0]
            else:
                i -= 1
            if object == 'circle':
                x, y = getCo(d[i])
                i += 1
                x1, y1 = getCo(d[i])
                i += 1
                try:
                    hh = d[i].split("setFillColor")
                    fill = hh[1]
                    i += 1
                except:
                    pass
                try:
                    hh = d[i].split("setStrokeColor")
                    stroke = hh[1]
                    i += 1
                except:
                    pass
                objects.append(setCircle(x, y, (getR(x, y, x1, y1)), fill, stroke))
                continue
            if object == 'rectangle':
                x, y = getCo(d[i])
                i += 1
                x1, y1 = getCo(d[i])
                i += 1
                try:
                    hh = d[i].split("setFillColor")
                    fill = hh[1]
                    i += 1
                except:
                    pass

                try:
                    hh = d[i].split("setStrokeColor")
                    stroke = hh[1]
                    i += 1
                except:
                    pass

                objects.append(setRect(x, y, abs(int(x1) - int(x)), abs(int(y1) - int(y)), fill, stroke))
                continue

            if object == 'line':
                x, y = getCo(d[i])
                i += 1
                x1, y1 = getCo(d[i])
                i += 1
                try:
                    hh = d[i].split("setFillColor")
                    fill = hh[1]
                    i += 1
                except:
                    pass

                try:
                    hh = d[i].split("setStrokeColor")
                    stroke = hh[1]
                    i += 1
                except:
                    pass

                objects.append(setLine(x, y, x1, y1, fill, stroke))
                continue

    except:
        pass

    tags = canvas.get_header()
    for object in objects:
        if object.fill is None:
            object.fill = canvas.fill
        if object.stroke is None:
            object.stroke = canvas.stroke
        tags += object.get_tag()
    tags += canvas.get_footer()
    print(tags)
    return HttpResponse(str(tags))
