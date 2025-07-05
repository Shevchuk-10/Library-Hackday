import os

def find_files_by_ext(path, ext):
    result = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                result.append(os.path.join(root, f))
    return result
