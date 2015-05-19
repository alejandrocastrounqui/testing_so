from threading import Thread
import time

class Policia(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.__banco = None
        self.__departamento = None
        self.estoy_jubilado = False
        
    def run(self):
        Thread.run(self)
        while(not self.estoy_jubilado):
            self.revisar_banco()
            time.sleep(1)
            
    def permanecer_cerca(self):
        print 'policia en el banco'
        time.sleep(1)
            
    def revisar_banco(self):
        if(self.banco):
            self.banco.llega_policia(self)
            if self.banco.ladrones:
                self.arrestar_ladrones()
            else:
                self.permanecer_cerca()
            self.banco.se_va_policia(self)
        
    def arrestar_ladrones(self):
        for ladron in self.banco.ladrones:
            self.banco.se_va_ladron(ladron)
            ladron.a_la_carcel()
        
    def jubilar(self):
        self.estoy_jubilado = True
                
    @property
    def departamento(self): return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento): self.__departamento = departamento
    
    @property
    def banco(self): return self.__banco
    
    @banco.setter
    def banco(self, banco): self.__banco = banco
    