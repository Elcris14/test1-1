class Circulo():

    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r

    def Area(self):
        area=3.14*(self.r**2)
        return area

    def Perimeter(self):
        perimetro= 2*(3.14)*self.r
        return perimetro

    def testBelongs(self,x,y):
        if(  (   ((self.a-x)**2)+ ((self.b-y)**2)  )  <= (self.r**2) ):
            print("Los puntos estan dentro del circulo")
        else:
            print("Los puntos no estan dentro del circulo")
    
circulo1 = Circulo(2,4,6)

print("El area es: ", circulo1.Area())
print("El area es: ", circulo1.Perimeter())
circulo1.testBelongs(8,15)