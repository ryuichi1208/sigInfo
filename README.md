# sigInfo - CLI tool to get and display process signal information

## About sigInfo

CLI tool to get and display process signal information

* SigPnd, SigBlk, SigIgn, SigCgt Display converted from binary notation
* Reference documentation for /proc/${pid}/status

## Supported OSes
- Linux

## Required
- python 3.6 ~

## Usage

``` bash
usage: Usage: siginfo.py

optional arguments:
  -h, --help            show this help message and exit
  -f PID_FILE, --file PID_FILE
                        concatnate target file name
  -p PIDF, --pid PIDF   concatnate target pid
  -d DOC, --doc DOC     Display documentation about signals
```
