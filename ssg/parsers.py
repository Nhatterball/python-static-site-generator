from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions : List[str] = []

    def valid_extension(self, exstension):
        return exstension in self.extensions

    def parse(self, path, source, dest):
        raise NotImplementedError()

    def read(self,path):
        with open(path, "r") as file:
            return file.read()
        
    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(path, "w") as file:
            return file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self,path,source,dest):
        self.copy(path, source, dest)
