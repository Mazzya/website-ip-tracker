import socket as s
import whois
import requests
import argparse
from io import open
from pdf_module.pdf_core import PdfReport

VERSION = '1.3.0'
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
                                @@@@@@@@@@@@/
                                  @@@@@@@@@@@@@   
                                    @@@@@@@@@@@@ 
                                      @@@@@@@@@@@
                                         (@@@@@@  
"""


def verify_domain() -> bool:
    """Check if there is an internet connection"""
    connected = False
    try:
        r = requests.get("https://google.com")
        if r.status_code == 200:
            connected = True
        else:
            print("Oops, check your internet connection")
    except:
        print("Oops, check your internet connection")
    finally:
        return connected


def format_list(ip_list) -> str:
    formatted_list = ', '.join(ip_list).replace("'", "").replace("[", "").replace("]", "")
    return formatted_list

def save_results(domain, ip, name_servers):
    """Save results in a .txt file"""
    with open('results.txt', 'a+') as f:
        f.write(f"{domain} : {ip} | {name_servers}" + '\n')


def track_website_ip(domain, save_file=False, pdf_report=False):
    """Tracks the IP address of the website passed as argument"""
    try:
        print(BANNER)
        if verify_domain():
            ip = s.gethostbyname_ex(domain)[2]
            try:
                domain_info = whois.whois(domain)
                name_servers = domain_info.name_servers
                #serva = format(name_servers)
            except TypeError:
                formatted_servers = ''
            #print(domain_info.name_servers)
            print(f"""
            Domain : {domain}
            IP : {format_list(ip)}
            LIST : {format_list(name_servers)}
""")
            
            # If user wants generate a .txt file to save results
            if save_file:
                save_results(domain, ip, formatted_servers)
            # If user wants generate a PDF report of results
            if pdf_report:
                format_pdf_name = f"Summary - {domain}"
                PdfReport(format_pdf_name, "Helvetica", 25, "Website IP Tracker", domain, ip)

    except s.gaierror:
        print("It seems that the domain does not exist or is not available at the moment.")
    except s.error as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the IP address and other stuff of any website")
    parser.add_argument('-d', '--domain', metavar='', type=str, required=False, help="Domain to track")
    parser.add_argument('-s', '--save', action='store_true', help="Save results in a file")
    parser.add_argument('--pdf', action='store_true', help="Generate a PDF report")
    parser.add_argument('--version', action='store_true', help="Current version")
    args = parser.parse_args()

    if args.domain and args.save and args.pdf:
        track_website_ip(args.domain, save_file=True, pdf_report=True)
    elif args.domain and args.save:
        track_website_ip(args.domain, save_file=True)
    elif args.domain and args.pdf:
        track_website_ip(args.domain, pdf_report=True)
    elif args.domain:
        track_website_ip(args.domain)
    elif args.version:
        print(f"Website IP Tracker {VERSION}")
    else:
        print("You need to write at least one argument, run 'tracker.py --help' to see what arguments are available.")
