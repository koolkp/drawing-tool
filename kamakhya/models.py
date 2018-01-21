from __future__ import unicode_literals

from django.db import models

from kamakhya import constants


# Create your models here.


class Canvas(models.Model):
    """
    Main container for the Creating a board
    """

    width = models.IntegerField()
    height = models.IntegerField()
    fill = models.CharField(max_length=7)
    stroke = models.CharField(max_length=7)
    stroke_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'canvas'

    def get_header(self):
        """
        for getting header
        :return: header
        """
        return str(constants.CANVAS_HEADER.format(width=self.width, height=self.height))

    @staticmethod
    def get_footer():
        """
        for getting the footer
        :return: footer
        """
        return constants.CANVAS_FOOTER


class Circle(models.Model):
    """
    model for circle
    """
    cx = models.IntegerField()
    cy = models.IntegerField()
    r = models.IntegerField()
    fill = models.CharField(max_length=7)
    stroke = models.CharField(max_length=7)
    strike_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'circle'

    def get_tag(self):
        """
        to get the specific tag for this
        :return: circle tag
        """
        return str(constants.CIRCLE_TAG.format(cx=self.cx, cy=self.cy, r=self.r, fill=self.fill, stroke=self.stroke))


class Line(models.Model):
    x1 = models.IntegerField()
    x2 = models.IntegerField()
    y1 = models.IntegerField()
    y2 = models.IntegerField()
    fill = models.CharField(max_length=7)
    stroke = models.CharField(max_length=7)
    strike_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'line'

    def get_tag(self):
        """
        to get the specific tag for this
        :return: line tag
        """
        return str(constants.LINE_TAG.format(x1=self.x1, x2=self.x2, y1=self.y1, y2=self.y2, fill=self.fill, stroke=self.stroke))


class Polygon(models.Model):
    points = models.CharField(max_length=7)
    fill = models.CharField(max_length=7)
    stroke = models.CharField(max_length=7)
    strike_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'polygon'

    def get_tag(self):
        """
        to get the specific tag for this
        :return: polygon tag
        """
        return str(constants.POLYGON.format(points=self.points, fill=self.fill, stroke=self.stroke))


class Rectangle(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    fill = models.CharField(max_length=7)
    stroke = models.CharField(max_length=7)
    strike_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rectangle'

    def get_tag(self):
        """
        to get the specific tag for this
        :return: rect tag
        """
        return str(constants.RECTANGLE.format(x=self.x, y=self.y, height=self.height, width=self.width, fill=self.fill, stroke=self.stroke))
