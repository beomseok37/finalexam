class Point:
    def __init__(self,a=0,b=0):
        self.__x=a
        self.__y=b
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance(self,b):
        x_distance=abs(self.__x-b.__x)
        y_distance=abs(self.__y-b.__y)
        result=(x_distance**2+y_distance**2)**0.5
        return result
    def __add__(self,other):
        print("[ "+str(self.__x+other.__x)+" , "+str(self.__y+other.__y)+" ]")
