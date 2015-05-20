from threading import Thread, Condition
from main.common.observable import observer
import time

@observer
class Ladron(Thread):

    def __init__(self, no_tengo_objetivo=None):
        Thread.__init__(self)
        self.__no_tengo_objetivo = no_tengo_objetivo or Condition()
        self.__hay_policias = Condition()
        self.__objetivo = None
        self.estoy_en_la_carcel = False
        
    def intentar_robo(self):
        if not self.objetivo.policias:
            self.objetivo.llega_ladron(self)
            print 'robando banco 2'
            time.sleep(0.2)
            print 'banco robado'
        
    def policias_en_movimiento(self, new_value, old_value, objetivo):
        print 'policias_en_movimiento'
        if not self.objetivo.policias:
            with self.__hay_policias:
                self.__hay_policias.notify_all()
            
    def run(self):
        Thread.run(self)
        with self.__no_tengo_objetivo:
            if not self.objetivo:
                self.__no_tengo_objetivo.wait()
        print 'observando'
        self.observe(self.objetivo, ['policias'], self.policias_en_movimiento)
        
        while(not self.estoy_en_la_carcel):
            with self.__hay_policias:
                self.__hay_policias.wait()
            self.intentar_robo()
            
            
    def a_la_carcel(self):
        self.estoy_en_la_carcel = True
        
    @property
    def objetivo(self): return self.__objetivo
    
    @objetivo.setter
    def objetivo(self, objetivo): 
        with self.__no_tengo_objetivo:
            self.__objetivo = objetivo
            self.__no_tengo_objetivo.notify_all()
        