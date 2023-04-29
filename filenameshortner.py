import os
import hashlib
from collections import defaultdict
import csv

src_folder = "D:\Working Files\Django Unicorn\docs"

def generate_md5(fname, chunk_size=1024):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        chunk = f.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    return hash.hexdigest()


if __name__ == "__main__":
    md5_dict = defaultdict(list)

    file_types_inscope = ["ppt", "pptx", "pdf", "docx", "txt", "html",
                          "mp4", "jpg", "png", "xls", "xlsx", "xml",
                          "vsd", "py", "json"]

    for path, dirs, files in os.walk(src_folder):
        print("Analyzing {}".format(path))
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types_inscope:
                file_path = os.path.join(os.path.abspath(path), each_file)
                md5_dict[generate_md5(file_path)].append(file_path)


    for key, val in md5_dict.items():
        first = True
        for file in val:
            if first:
                first = False
            else:
                os.remove(file)

    print("Done")

for i in os.listdir(src_folder):
    c = len(i)
    # print (i)
    if c > 50 :
        os.rename(os.path.join(src_folder, i),os.path.join(src_folder, i[:40])+'....'+ ".docx")
    else:
        pass