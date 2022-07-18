from pathlib import Path
import Typer
from ssg.site import Site

class Site:
    def site(self, source, dest):
        self.Path(source)
        self.Path(dest)

    def create_dir(self, path):
        directory = destination / relative_to(self.dest)/ relative_to(self.source)
        mkdir(directory, parents=True, exists_ok=True)

    def build():
        mkdir(self.dest, parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if path.isdir(path):
                create_dir(path)

