from main.common.observable import observable, notificable

@observable
class Banco(object):

    def __init__(self):
        self.__tesoro = 0
        self.__ladrones = []
        self.__policias = []
    
    def robadon(self):
        self.tesoro = 0
        
    def deposita_camion(self):
        self.tesoro += 100000
    
    def llega_ladron(self, ladron): 
        self.__ladrones.append(ladron)
        
    def se_va_ladron(self, ladron): 
        self.__ladrones.remove(ladron)
        
    @notificable(['policias'])
    def llega_policia(self, policia): 
        self.__policias.append(policia)
        
    @notificable(['policias'])
    def se_va_policia(self, policia): 
        self.__policias.remove(policia)
    
    @property
    def ladrones(self): return self.__ladrones
    
    @property
    def policias(self): return self.__policias
    
    @property
    def tesoro(self): return self.__tesoro
    
    @tesoro.setter
    def tesoro(self, tesoro): self.__tesoro = tesoro
    
    
    