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
import argparse

folders = [ 
            'source' ,
            'docs'   ,
            'config' ,
            'example',
            'test'   , 'test/unit-test',
            'library',
            'project',
            'tools'
          ]

def main():

    parser = argparse.ArgumentParser (
        prog="project-folder", description="simple project folder structure creation tool")
    parser.add_argument ("-d", "--directory",
                        help="software project folder orgnatation tool",
                        type=str, required=True)

    args = vars(parser.parse_args())

    for folder in folders:
        path = args['directory'] + '/' +folder
        try:
            os.makedirs(path)
            print ('folder create -', path)
        except FileExistsError:
            print ('folder exist  -', path)

if __name__ == "__main__":
    main ()
