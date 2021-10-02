from backend import handle_search

files_found = handle_search.find_files("c:/temp", "up")
for f in files_found:
    print(f.name, f.size)
#~ print("Found:", files_found)