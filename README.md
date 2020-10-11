# yts-lists
Download list of torrents using V2 API from YTS

## Requirements
1. Python 3.x (tested on 3.8) for getting download list of torrents
2. Wget for downloading .torrent from URL

## Steps
1. Run main.py
2. [Run](https://stackoverflow.com/a/52916930/5726675)
```console
foo@bar:~$ wget --content-disposition --no-clobber --trust-server-names -i yts.txt
```

## TODO
+ Use python scripting for automation
+ Use cross platform alternative to Wget (or implement Invoke-WebRequest for powershell)
+ Speed up code execution
+ Add progress meters
+ Add user input options for preferred file type
