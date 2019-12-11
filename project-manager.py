#!/usr/bin/env python

#*****************************************************************************
# ______  _                             ___  ___        _               
# | ___ \(_)                            |  \/  |       | |              
# | |_/ / _  _ __    __ _  _ __  _   _  | .  . |  __ _ | | __ ___  _ __ 
# | ___ \| || '_ \  / _` || '__|| | | | | |\/| | / _` || |/ // _ \| '__|
# | |_/ /| || | | || (_| || |   | |_| | | |  | || (_| ||   <|  __/| |   
# \____/ |_||_| |_| \__,_||_|    \__, | \_|  |_/ \__,_||_|\_\\___||_|   
#                                 __/ |                                 
#                                |___/                                  
#                                                                       
# Copyright (C) 2019 Binary Maker - All Rights Reserved
#
# This program and the accompanying materials are made available
# under the terms described in the LICENSE file which accompanies
# this distribution.
# Written by Binary Maker <https://github.com/binarymaker>
#*****************************************************************************

import os
import sys
import argparse
import subprocess
import time
import json

def file_create(file_name, file_text):
    if(os.path.exists(file_name)):
        print("file exists", file_name)
    else:
        proj_file = open(file_name,'w')
        proj_file.write(file_text)
        proj_file.close()
        print("file created", file_name)

def execute(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE,bufsize=1)
    lines_iterator = iter(popen.stdout.readline, b"")
    while popen.poll() is None:
        for line in lines_iterator:
            nline = line.rstrip()
            print(nline.decode("latin"), end = "\r\n",flush =True) # yield line

def main():

    parser = argparse.ArgumentParser (
        prog="project-manager", description="project folder structure creation tool")
    parser.add_argument ("-d", "--directory",
                        help="project folder directory",
                        type=str, required=True)
    parser.add_argument ("-f", "--folder", action='store_true',
                        help="project controller platform"
                        )
    parser.add_argument ("-g", "--gitinit", action='store_true',
                        help="git init"
                        )
    parser.add_argument ("-gu", "--gituser", action='store_true',
                        help="git user profile config from setting.json"
                        )
    parser.add_argument ("-p", "--platform",
                        help="project controller platform"
                        )
    
    print ('-' * 30)
    
    args = vars(parser.parse_args())
    script_dir = os.getcwd()

    with open('setting.json') as f:
        settings = json.load(f)

    if (args['folder']):
        print ('Project folder structure')
        print ('------------------------')
        for folder in settings["project_folders"]:
            path = args['directory'] + '/' +folder
            try:
                os.makedirs(path)
                print ('folder create -', path)
            except FileExistsError:
                print ('folder exist  -', path)
        
        for files in settings["project_files"]:
            path = args['directory'] + '/' + files["name"]
            file_create(path, files["text"])

    if (args['gitinit']):
        os.chdir(args['directory'])
        execute('git init')
        os.chdir(script_dir)
        
    if (args['gituser']):
        os.chdir(args['directory'])
        subprocess.call('git init', shell=True)
        git_config = settings["git_config"]
        execute("git config user.name "+ git_config["name"])
        print ("git user name  :", git_config["name"])
        execute("git config user.email "+ git_config["email"])
        print ("git user email :", git_config["email"])
        os.chdir(script_dir)
        
    if (args['platform']):
        os.chdir(args['directory'])
        execute('sh '+script_dir+'\project-atmega.sh')
        os.chdir(script_dir)
    
if __name__ == "__main__":
    main ()
