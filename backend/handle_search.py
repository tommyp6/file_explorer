from . import get_files
from frontend import get_search
import os


def find_files():
    files = get_files()
    user_search = get_search()
    files_found = []
    for file in files[user_search]:
        if file == os.path.basename(user_search):
            files_found.append(file)