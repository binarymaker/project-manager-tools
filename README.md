# Project script tools

Automated standard project folder structure generation python scripts.

```plantuml
@startsalt
{
  {T
   + <>project-folder
   ++ **source**
   ++ **docs**
   ++ **config**
   +++ sub modules cfg files
   ++++ sub-module1-cfg.h
   ++++ sub-module2-cfg.h
   ++ **example**
   +++ Implementation 1
   +++ Implementation 2
   ++ **test**
   +++ unit-test
   ++ **library**
   +++ sub modules
   +++ 3rd party library
   ++ **project**
   ++ **tools**
   ++ <color:green>scripts</color>
   +++ project-folder.py
   +++ smake.py
   + LICENSE
   + README.md
  }
}
@endsalt
```

## project-folder

[project-folder.py](/scripts/project-folder.py) : Generate standard folder structure in initial project workplace.

### Usage 
```shell
> python3 project-folder [-d DIRECTORY]

[-d DIRECTORY] -- required. Project folder structure create location
```


### Example 
```shell
# Create folders in previews path
> python3 project-folder.py -d .. 
```

## smake

[smake.py](/scripts/smake.py) : Generate C/C++ source and header files.


### Usage 
```shell
> python3 smake [-f FILE_NAME] [-d DIRECTORY] [-s SMART]

[-f FILE_NAME] -- required.
[-d DIRECTORY] -- optional. Source file create location
[-s SMART]     -- optional. Source file create in source and config folder 
                  as per project-folder.py folder structure
```

### Example 
```shell
# Create source template file in current folder
> python3 project-folder.py -f app

# Create source template file in previews path
> python3 project-folder.py -f app -d ..

# Create source template file in previews path source and config folders
> python3 project-folder.py -f app -d .. -s Y
```