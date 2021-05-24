# Website IP Tracker
![GitHub](https://img.shields.io/github/license/mazzya/website-ip-tracker) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/mazzya/website-ip-tracker)
### Find the IP address of any website.
WIT ( Website IP Tracker ) is a script that allows you to quickly track the IP addresses of websites.

Visit [Change Log](https://github.com/Mazzya/website-ip-tracker/blob/main/CHANGELOG.md)
## Usage
```
usage: tracker.py [-h] [-d] [-s] [--pdf]

optional arguments:
    -h, --help          show this help message and exit
    -d, --domain        domain to track
    -s, --save          save results in a file
    --pdf               generate a PDF report
```
## Example
```
$ tracker.py -d www.google.com

        @@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@             @@@@@@@@
  @@@@@@@                   @@@@@@@
 @@@@@@                       @@@@@@
 @@@@@/       Website IP      ,@@@@@
 @@@@@          Finder         @@@@@,
 @@@@@                         @@@@@
 @@@@@@                       @@@@@@
  @@@@@@                     @@@@@@
   @@@@@@@@               &@@@@@@@
     @@@@@@@@@@%     #@@@@@@@@@@@@&@@        Developed by Mazzya
        @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@        Version 1.0.0
             @@@@@@@@@@@      @@@@@@@@@@@@         github.com/mazzya
                                @@@@@@@@@@@@/         mazzya.tk
                                  @@@@@@@@@@@@@
                                    @@@@@@@@@@@@
                                      @@@@@@@@@@@
                                         (@@@@@@


            Domain : www.google.com
            IP : 142.250.74.228
```
You can also save the results in a text file with the argument ```-s``` or ```--save```.

The file is saved in the same directory as the script and has the following format :
> Domain : IP
