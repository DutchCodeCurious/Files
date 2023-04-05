import os
from zipfile import ZipFile
from pathlib import Path

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


cache = "files/cache"


def clean_cache():
    cache = "files/cache"
    if not os.path.exists(cache):
        os.mkdir(cache)
    for file_name in os.listdir(cache):
        file = cache + "/" + file_name
        if os.path.isfile(file):
            os.remove(file)
    return


def cache_zip(zip_file, cache_path):
    with ZipFile(zip_file, 'r') as zObject:
        zObject.extractall(path=cache_path)
    return


def cached_files():
    all_files = []
    parent_dir = os.getcwd()
    abs_path = f'{parent_dir}/files/cache/'
    for file_name in os.listdir(cache):
        fpath = os.path.abspath(f'{abs_path}{file_name}')
        all_files.append(fpath)
    return all_files


def find_password(lijst):
    for files in lijst:
        with open(files, "r") as f:
            word = f.readlines()
            for line in word:
                if "password" in line:
                    pass_w = line.split(" ")[1]
                    password = pass_w.split('\n')[0]
    return password


clean_cache()
#cache_zip()
cached_files()
#find_password()
