import socket as s
import requests
import argparse
from io import open

VERSION = '1.0.0'
BANNER = f"""                           
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
        @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@        Version {VERSION}       
             @@@@@@@@@@@      @@@@@@@@@@@@         github.com/mazzya     
                                @@@@@@@@@@@@/         mazzya.tk
                                  @@@@@@@@@@@@@   
                                    @@@@@@@@@@@@ 
                                      @@@@@@@@@@@
                                         (@@@@@@  
"""

def verify_internet() -> bool:
    """Check if there is an internet connection"""
    try:
        connected = False
        r = requests.get("https://google.com")
        if r.status_code == 200:
            connected = True
        else:
            print("Oops, check your internet connection")
        return connected
    except:
        print("Oops, check your internet connection")

def track_website_ip(domain, save_file=False):
    """Tracks the IP address of the website passed as argument"""
    try:
        print(BANNER)
        if (verify_internet()):
            ip = s.gethostbyname(domain)
            print(f"""
            Domain : {domain}
            IP : {ip}""")
            if save_file is True:
                save_results(domain, ip)
    except s.gaierror:
        print("Domain failed, try again please")

def save_results(domain, ip):
    """Save results in a .txt file"""
    with open('results.txt', 'a+') as f:
        f.write(f"{domain} : {ip}" + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the IP address of any website")
    parser.add_argument('-d', '--domain', metavar='', type=str, required=True, help="Domain to track")
    parser.add_argument('-s', '--save', action='store_true', help="Save results in a file")
    args = parser.parse_args()

    if args.domain and args.save:
        track_website_ip(args.domain, save_file=True)

    elif args.domain:
        track_website_ip(args.domain)