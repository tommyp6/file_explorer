import os
from pathlib import Path as _Path

HOME = os.path.expanduser("~")


class File:
    def __init__(self, path, size, last_modified, owner, group):
        self.path = path
        self.name = os.path.basename(path)
        self.size = size
        self.last_modified = last_modified
        self.owner = owner
        self.group = group

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.size}\t{self.owner}:{self.group}\t{self.last_modified}\t{self.name}"


class Path:
    def __init__(self, path):
        self.path = path
        self.folders = []
        self.files = []

    def __iter__(self):
        self.items()

        for folder in self.folders:
            yield folder

        for file in self.files:
            yield file

    def __str__(self):
        return self.path

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.path}"

    def items(self):
        for item in os.listdir(self.path):
            item = os.path.join(self.path, item)
            if os.path.isfile(item):
                _p = _Path(item)
                file = File(
                    item,
                    os.path.getsize(item),
                    os.path.getctime(item),
                    _p.owner(),
                    _p.group(),
                )
                self.files.append(file)

            elif os.path.isdir(item):
                folder = Folder(os.path.join(self.path, item), item)
                self.folders.append(folder)

        return [*self.folders, *self.files]


class Folder(Path):
    def __init__(self, path, name):
        super().__init__(path)
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.name}"


if __name__ == "__main__":
    pwd = os.path.dirname(os.path.abspath(__file__))
    p = Path(os.path.join(pwd, "testdir"))

    for item in p.items():
        print(repr(item))
        if isinstance(item, Folder):
            for i in item:
                print("\t", repr(i))
