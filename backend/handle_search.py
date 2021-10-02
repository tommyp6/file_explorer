'''The main purpose of the find_files function is to return a list of
paths which can then be displayed using the gui. The first parameter of find_files
is a dictionary with keys of paths and values of lists including further dictionaries.
The second parameter is a string the user searched.'''

# from . import get_files
# from frontend import get_search
import os
import backend

def find_files(dirpath, user_search):
    path = backend.Path(dirpath)
    # files = get_files()
    # user_search = get_search()
    files_found = []
    for file in path: ## files[user_search]:
        if user_search in os.path.basename(file.name):
            files_found.append(file)

    #~ files_found = [file for file in files[user_search] if file == os.path.basename(user_search)]

    return files_found


if __name__ == "__main__":
    files = {"hello.txt":[], "world.txt":[]}
    user_search = "hello.txt"
    print(find_files(files, user_search))
