from functools import wraps
from __builtin__ import int, str, bool

def observer(instance):
    def add_listener(self, listener):
        self.listeners.append(listener)
    instance.add_listener = add_listener
    def observe(self, observable_instance, attributes, callback):
        observable_instance.add_listener(self, attributes, callback)
    instance.observe = observe
    return instance

class AttributeListener():
    def __init__(self, _listener, _callback):
        self.listener = _listener
        self.callback = _callback
    def invoke(self, new_value, old_value, _observable):
        #callback is binded to observer yet
        self.callback(new_value, old_value, _observable)

def observable(instance):
    instance.attributes = {}
    
    def append_to_attribute(self, attribute, attributeListener):
        if not attribute in self.attributes:
            self.attributes[attribute] = []
        self.attributes[attribute].append(attributeListener)
         
    def add_listener(self, listener, __attributes, callback):
        print self
        if not __attributes:
            pass #throw exception
        for attribute in __attributes:
            self.append_to_attribute(attribute, AttributeListener(listener, callback))
            
    def notify_all(self, attribute, new_value, old_value):
        if attribute in self.attributes:
            listeners = self.attributes[attribute]
            for listener in listeners:
                listener.invoke(new_value, old_value, self)
            
    instance.append_to_attribute = append_to_attribute    
    instance.add_listener = add_listener
    instance.notify_all = notify_all
    return instance


class Control():
    
    def __init__(self, _attribute_name):
        self.attribute_name = _attribute_name
        self.value = None
    
    def watch(self, observable_instance):
        self.value = getattr(observable_instance, self.attribute_name)
    
    def check(self, observable_instance):
        old_value = self.value
        new_value = getattr(observable_instance, self.attribute_name)
        primitive = (int, str, bool)
        if type(new_value) in primitive:
            if not (new_value is old_value):
                observable_instance.notify_all(self.attribute_name, new_value, old_value)
        else:
            observable_instance.notify_all(self.attribute_name, new_value, old_value)

class notificable():
    
    def __init__(self, attribute_names):
        print self
        self.controls = []
        for attribute_name in attribute_names:
            self.controls.append(Control(attribute_name))
    
    def watch(self, owner):
        for control in self.controls:
            control.watch(owner)
            
    def check(self, owner):
        for control in self.controls:
            control.check(owner)
        
    def __call__(self, method):
        print self
        @wraps(method)
        def notificable_method(owner, *arg):
            self.watch(owner)
            result = method(owner, *arg)
            self.check(owner)
            return result
        return notificable_method
    
    