import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping

class content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(cls, string):
        _ = __regex.split(string, 2)
        fm = __regex.split(string, 2)
        content = __regex.split(string, 2)

        load(fm, Loader = FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content" : content}

    @property
    def body():
        return self.data["content"]

    @property
    def type():
        if self.data["type"] is None:
            return None
        else:
            return self.data["type"]
    
    @type.setter(self.data["type"])

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)




