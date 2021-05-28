class laptob:   
      def __init__(self, price=0, model=0):
            self._price =price 
            self._model = model 
      def setprice(self, price):
            self._price = price 
      def setmodel(self, model):  
            self._model = model  
      def getprice(self):  
           return self._price  
      def getmodel(self): 
           return self._model 
      def __str__(self): 
           return "price: "+str(self._price)+"- Model: "+str(self._model)
class toshiba(laptob):
      def __init__(self,price=0, model=0,co=""): 
            super().__init__(price,model) 
            self._co = co
      def info(self):     
          print("The info of this laptob is: 2019japan" ) 
class asus(laptob): 
     def info(self):  
         print("The info of this laptob is: 2018asus") 
 
laptob1 = toshiba(600,2019,"japan")
laptob2 = asus(500,2018)
print(laptob1)
print(laptob2)
laptob1.info()
laptob2.info()
print("laptob1:")
print(laptob1.getprice())
print(laptob1.getmodel()) 
print() 
print(laptob2)



#A program that presents the state of inheritance in the different types of laptops and shows their different characteristics
