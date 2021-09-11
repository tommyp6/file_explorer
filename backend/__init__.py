import os

HOME = os.path.expanduser("~")


def get_files(directory=HOME):
    """
    files = [ "dir" : {
        "file": {},    
    }]
    """
    files = []
    for file in os.walk(directory):
        

    return


if __name__ == "__main__":
    get_files("../testdir")
