#!/usr/bin/env python3
# coding: utf-8

import sys
import glob
import os
import shutil
import re

args = sys.argv
if len(args) != 3:
    sys.exit()

src = args[1]
dest = args[2]

def main():
    # copy src directory to dest directory
    print("copying", src, "directory to", dest, "directory...")
    shutil.copytree(src, dest, dirs_exist_ok=True)

    # remove src directory mp3 files
    for root, dirs, files in os.walk(dest):
        for file in files:
            if file.endswith((".mp3", ".MP3")):
                dest_file_path = os.path.join(root, file)

                # replace dest path to src path
                src_file_path = re.sub(r'^'+dest, src, dest_file_path)

                # copy dest file to src file
                print("removing", src_file_path, "...")
                os.remove(src_file_path)

    # sort filename and copy dest directory to src directory
    for root, dirs, files in os.walk(dest):
        files.sort()
        for file in files:
            if file.endswith((".mp3", ".MP3")):
                dest_file_path = os.path.join(root, file)

                # replace dest path to src path
                src_file_path = re.sub(r'^'+dest, src, dest_file_path)

                # copy dest file to src file
                print("copying", dest_file_path, "to", src_file_path, "...")
                shutil.copy(dest_file_path, src_file_path)

if __name__=='__main__':
    main()
