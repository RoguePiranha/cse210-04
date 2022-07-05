from casting.actor import Actor
from shared.point import Point


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._value = 0

    def set_value(self):
        if self._text == "*":
            self._value = 1


        elif self._text == "o":
            self._value = -1

    def get_value(self):
        
        return self._value
