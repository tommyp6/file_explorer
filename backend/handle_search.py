# from . import get_files
# from frontend import get_search
import os


def find_files(files, user_search):
    # files = get_files()
    # user_search = get_search()
    files_found = []
    for file in files[user_search]:
        if file == os.path.basename(user_search):
            files_found.append(file)

    files_found = [file for file in files[user_search] if file == os.path.basename(user_search)]

    return files_found


if __name__ == "__main__":
    files = {"hello.txt":[], "world.txt":[]}
    user_search = "hello.txt"
    print(find_files(files, user_search))
