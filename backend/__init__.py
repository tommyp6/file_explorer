import os
from pathlib import Path as _Path

HOME = os.path.expanduser("~")


class Path:
    def __init__(self, path, size=None, last_modified=None, owner=None, group=None):
        self.path = path
        self.name = os.path.basename(path)
        self.size = size
        self.last_modified = last_modified
        self.owner = owner
        self.group = group

        if self.size is None:
            self.size = os.path.getsize(self.path)

        if self.last_modified is None:
            self.last_modified = os.path.getctime(self.path)

        if self.owner is None:
            self.owner = None ## _Path(self.path).owner()

        if self.group is None:
            self.group = None ## _Path(self.path).group()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.type()}> {self.size}\t{self.owner}:{self.group}\t{self.last_modified}\t{self.name}"

    def __iter__(self):
        if not os.path.isfile(self.path):
            for item in os.listdir(self.path):
                item = os.path.join(self.path, item)
                _p = _Path(item)
                base = Path(
                    item,
                    os.path.getsize(item),
                    os.path.getctime(item),
                    None, ## _p.owner(),
                    None ## _p.group(),
                )
                yield base

    def type(self):
        if os.path.isfile(self.path):
            return "File"

        if os.path.isdir(self.path):
            return "Folder"


if __name__ == "__main__":
    pwd = os.path.dirname(os.path.abspath(__file__))
    p = Path(os.path.join(pwd, "testdir"))

    # Go 1 level deep.
    print(repr(p))
    for item in p:
        print(f"\t{repr(item)}")
        for i in item:
            print(f"\t\t{repr(i)}")
