# Website IP Tracker
![GitHub](https://img.shields.io/github/license/mazzya/website-ip-tracker) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/mazzya/website-ip-tracker)
### Find the IP address of any website.
WIT ( Website IP Tracker ) is a script that allows you to quickly track the IP addresses of websites.

Visit [Change Log](https://github.com/Mazzya/website-ip-tracker/blob/main/CHANGELOG.md)
## Requirements
```
Python 3
pip install reportlab
```
## Clone the repository
```
$ git clone https://github.com/Mazzya/website-ip-tracker.git
```
If you don't want to clone it, you can download it directly from [here](https://github.com/Mazzya/website-ip-tracker/releases).

Once you have the project locally, you need to go to the application folder and run ```tracker.py```
## Usage
```
usage: tracker.py [-h] [-d] [-s] [--pdf]

optional arguments:
    -h, --help          show this help message and exit
    -d, --domain        domain to track
    -s, --save          save results in a file
    --pdf               generate a pdf report
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
You can also save the results in a text file with the argument ```-s``` or ```--save```.  If you want generate a PDF report with the results, you can use ```--pdf```

The file and PDF report is saved in the same directory as the script and has the following format :
> Domain : IP
