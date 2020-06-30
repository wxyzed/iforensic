from __future__ import print_function
import argparse
from datetime import datetime as dt
import os
import sys
import hashlib #Hash lib
import logging
from collections import Counter
import shutil

print("""
  __    ___    __    _           __    _      ___       ____  _      ____
 / /\  | | \  / /\  | |\/|      / /\  | |\ | | | \     | |_  \ \  / | |_
/_/--\ |_|_/ /_/--\ |_|  |     /_/--\ |_| \| |_|_/     |_|__  \_\/  |_|__

""")

__authors__ = ["Adam Doukani"]
__date__ = "1st July, 2020"
__description__ = "Digital Forensics Tool"
parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {} on {}".format(__authors__, __date__)
)
def __hashing__():
    available_algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }
    args = parser.parse_args()
    input_file = str(input("Specify file directory: "))
    hash_alg = input("Specify hashing algorithm <md5 | sha1 | sha256 | sha521> : ")
    file_name = available_algorithms[hash_alg]()
    abs_path = os.path.abspath(input_file)
    file_name.update(abs_path.encode())


    print("The {} of the filename is: {}".format(
    hash_alg, file_name.hexdigest()))
    file_content = available_algorithms[hash_alg]()
    with open(input_file, 'rb') as open_file:
        buff_size = 1024
        buff = open_file.read(buff_size)

        while buff:
            file_content.update(buff)
            buff = open_file.read(buff_size)

    print("The {} of the content is: {}".format(
        hash_alg, file_content.hexdigest()))

def __help__():
    print("""
    Still in progress ...
    """)

def __sysinfo__():
    file_path = str(input("Specify file directory: "))
    stat_info = os.stat(file_path)
    if "linux" in sys.platform or "darwin" in sys.platform:
        print("Change time: ", dt.fromtimestamp(stat_info.st_ctime))
    elif "win" in sys.platform:
        print("Creation time: ", dt.fromtimestamp(stat_info.st_ctime))
    else:
        print("[-] Unsupported platform {} detected. Cannot interpret "
              "creation/change timestamp.".format(sys.platform)
              )
    print("Modification time: ", dt.fromtimestamp(stat_info.st_mtime))
    print("Access time: ", dt.fromtimestamp(stat_info.st_atime))

    print("File mode: ", stat_info.st_mode)
    print("File inode: ", stat_info.st_ino)
    major = os.major(stat_info.st_dev)
    minor = os.minor(stat_info.st_dev)
    print("Device ID: ", stat_info.st_dev)
    print("\tMajor: ", major)
    print("\tMinor: ", minor)
    print("Number of hard links: ", stat_info.st_nlink)
    print("Owner User ID: ", stat_info.st_uid)
    print("Group ID: ", stat_info.st_gid)
    print("File Size: ", stat_info.st_size)
    # Gather other properties
    print("Is a symlink: ", os.path.islink(file_path))
    print("Absolute Path: ", os.path.abspath(file_path))
    print("File exists: ", os.path.exists(file_path))
    print("Parent directory: ", os.path.dirname(file_path))
    print("Parent directory: {} | File name: {}".format(
        *os.path.split(file_path)))

print("Choose an option: ")
print("\n0- Exit")
print("1- TimeStamp")
print("2- File Hash")
print("99- Help\n")
args = parser.parse_args()
mode_on = True
while mode_on:
    choice = int(input("Choose: "))
    if choice == 1:
        __sysinfo__()
    elif choice == 2:
        __hashing__()
    elif choice == 0:
        print("Adam and Eve send their regards!")
        break
    elif choice == 99:
        __help__()
    else:
        print("Humm that wasn't listed")
