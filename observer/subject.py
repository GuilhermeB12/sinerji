from typing import List
from .observer_base import Observer
from abc import ABC

class LLMResponsePublisher(ABC):
    def __init__(self):
        self._observers: List[Observer] = []
        self._chosen_response_info = None

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

    @property
    def chosen_response_info(self):
        return self._chosen_response_info

    @chosen_response_info.setter
    def chosen_response_info(self, value):
        self._chosen_response_info = value
        self.notify(value)