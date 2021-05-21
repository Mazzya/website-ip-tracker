# Website IP Tracker
### Find the IP address of any website.
WIT ( Website IP Tracker ) is a script that allows you to quickly track the IP addresses of websites.
## Usage
```
usage: tracker.py [-h] [-d] [-s]

optional arguments:
    -h, --help          show this help message and exit
    -d, --domain        domain to track
    -s, --save          save results in a file
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
