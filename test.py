from circle import Circle
from line import Line
from point import Point
from polygon import Polygon
from rectangle import Rectangle
from square import Square
from triangle import Triangle

aylana=Circle(6)
a=aylana.getLength()
b=aylana.getLength()
# print(a)
# print(b)
chiziq=Line(6,9,3,5)
a=chiziq.get_length()
# print(a)
nuqta=Point(8,6)
d=nuqta.distance_from_Ycoordinate()
e=nuqta.getQuadrant()
c=nuqta.on_Xcoordinate()
w=nuqta.on_Ycoordinate()
# print(d)
# print(e)
# print(c)
# print(w)
kupburchak=Polygon(7,3)
g=kupburchak.getArea()
h=kupburchak.getPerimeter()
# print(g)
# print(h)
turtburchaklar=Rectangle(8,2)
k=turtburchaklar.getArea()
k2=turtburchaklar.getPerimeter()
# print(k)
# print(k2)

kvadrat=Square(8)
kv=kvadrat.getArea()
kvp=kvadrat.getPerimeter()
# print(kv)
# print(kvp)
trian=Triangle(6,8,10)
trian_getarea=trian.getArea()
trian_getperim=trian.getPerimeter()
print(trian_getarea)
# print(trian_getperim)
