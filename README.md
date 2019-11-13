# Project script tools

Automated standard project folder structure generation python scripts.

```
    project-folder
 ---|-------------------------------- # Auto generated folders
 |  +-- source                      |
 |  +-- docs                        |
 |  +-- config                      |
 |  +-- example                     |
 |  +-- test                        |
 |      +-- unit-test               |
 |  +-- library                     |
 |  +-- project                     |
 |  +-- tools                       |
 ---|--------------------------------
    +-- scripts                      #(1) Copy script folder from repo to project-folder
        +-- setting.json             #(2) modify folder structure and git user configuration
        +-- project-manager.py       #(3) run to generate std folders and files
        +-- smake.py                 #(4) run to generate .c/.h files
    +-- README.md                    # Auto generated file
```

## project-manager

[project-manager.py](scripts/project-manager.py) : Generate standard folder structure for initiate project workplace.

### Usage 
```shell
> python3 project-manager [-d DIRECTORY] [-g --git]

Required arguments:
    [-d DIRECTORY] -- project folder directory
Optional arguments:
    [-g --git]     -- git auto initialization.
    [-h]           -- Help
```

### Example 
```shell
# Create folders in previews path
> python3 project-manager.py -d .. 
```

## smake

[smake.py](scripts/smake.py) : Generate C/C++ source and header files.

### Usage 
```shell
> python3 smake [-f FILE_NAME] [-d DIRECTORY] [-s SMART]

Required arguments:
    [-f FILE_NAME] --  library file name
Optional arguments:
    [-d DIRECTORY] -- Source file create location
    [-s SMART]     -- Source file create in source and config folder 
                        as per project-manager.py folder structure
```
### Example 
```shell
# Create source template file in current folder
> python3 smake.py -f app

# Create source template file in previews path
> python3 smake.py -f app -d ..

# Create source template file in previews path source and config folders
> python3 smake.py -f app -d .. -s
```

## Customization

* Fork https://github.com/binarymaker/project-manager-tools (this repo) to your account
* clone repo from your account
```
> git clone https://github.com/<your_username>/project-manager-tools.git (your repo)
```
* Modify [setting.json](scripts/setting.json)

```json
{
  
  "git_config":{
      "name" : "binarymaker",
      "email": "importfunfromcode@gmail.com"
  },

  "project_folders":[
                    "source"  ,
                    "docs"    ,
                    "config"  ,
                    "example" ,
                    "test"    , "test/unit-test",
                    "library" ,
                    "project" ,
                    "tools"
  ],

  "project_files":[
    {
      "name": "README.md",
      "text": ""
    }
  ]
}
```

* modify [smake.py](scripts/smake.py) for source file template
```python
copyright_tmpl = \
"""/**\cond
  ******************************************************************************
  * ______  _                             ___  ___        _               
  * | ___ \(_)                            |  \/  |       | |              
  * | |_/ / _  _ __    __ _  _ __  _   _  | .  . |  __ _ | | __ ___  _ __ 
  * | ___ \| || '_ \  / _` || '__|| | | | | |\/| | / _` || |/ // _ \| '__|
  * | |_/ /| || | | || (_| || |   | |_| | | |  | || (_| ||   <|  __/| |   
  * \____/ |_||_| |_| \__,_||_|    \__, | \_|  |_/ \__,_||_|\_\\\\___||_|   
  *                                 __/ |                                 
  *                                |___/                                  
  *                                                                       
  * Copyright (C) """ + year + """ Binary Maker - All Rights Reserved
  *
  * This program and the accompanying materials are made available
  * under the terms described in the LICENSE file which accompanies
  * this distribution.
  * Written by Binary Maker <https://github.com/binarymaker>
  ******************************************************************************
  \endcond*/
"""
```
* push change to online 
```
> git push origin
```
