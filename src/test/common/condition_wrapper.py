from threading import Condition
class ConditionWrapper():
    
    def __init__(self, listener=None):
        self.__listeners = []
        if(listener):
            self.add(listener)
        self.__condition = Condition()
        self.__waiting_event = object()
        self.__notify_event = object()
        self.__notify_all_event = object()
            
    def add(self, listener):
        self.__listeners.append(listener)
        
    def wait(self):
        print "wait"
        for listener in self.__listeners:
            listener.append(self.__waiting_event)
        self.__condition.wait()
        
    def notify_all(self):
        for listener in self.__listeners:
            listener.append(self.__notify_all_event)
        self.__condition.notify_all()
        
    def notify(self):
        for listener in self.__listeners:
            listener.append(self.__notify_event)
        self.__condition.notify()
        
    def __enter__(self):
        return self.__condition.__enter__()
    
    def __exit__(self, *args):
        return self.__condition.__exit__(*args)

    @property
    def waiting_event(self):
        return self.__waiting_event

    @property
    def notify_all_event(self):
        return self.__notify_all_event

    @property
    def notify_event(self):
        return self.__notify_event
    
    
    