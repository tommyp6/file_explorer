import os

HOME = os.path.expanduser("~")


def get_files(directory=HOME):
    """
    files = {
        "filename":
    }
    """
    files = {}
    for file in os.walk(directory):
        print(file)

    return


if __name__ == "__main__":
    get_files("../testdir")
