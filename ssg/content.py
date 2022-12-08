import re

from yaml import FullLoader, load

from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)
    
    def __init__(self, metadata, content) -> None:
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return None if "type" not in self.data else self.data["type"] 

    @type.setter
    def type(self):
        self.data = self.data["type"]

    def __getitem__(self, __key):
        return self.data[__key]

    def __iter__(self):
        return super().__iter__()