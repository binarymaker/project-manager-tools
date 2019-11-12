# Project script tools

Automated standard project folder structure generation python scripts.

```
      project-folder
 ------------------------------------ # Auto generated folders
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
    +-- scripts                      #(1) initial Copy/paste to project-folder
        +-- project-manager.py       #(2) run to generate std folders
        +-- smake.py                 #(3) run to generate .c/.h files
    +-- LICENSE                      #(1) initial Copy/paste to project-folder 
    +-- README.md
```

## project-manager

[project-manager.py](project-manager.py) : Generate standard folder structure for initial project workplace.

### Usage 
```shell
> python3 project-manager [-d DIRECTORY] [-g --git]

Required arguments:
    [-d DIRECTORY] -- project folder directory
Optional arguments:
    [-g --git]   -- git auto initialization.
    [-h]         -- Help
```


### Example 
```shell
# Create folders in previews path
> python3 project-manager.py -d .. 
```

## smake

[smake.py](smake.py) : Generate C/C++ source and header files.


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

## Customization

* Fork https://github.com/binarymaker/project-manager-tools (this repo) to your account
```
> git clone https://github.com/<your_username>/project-manager-tools.git (your repo)
```
* Modify [setting.json](setting.json)

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