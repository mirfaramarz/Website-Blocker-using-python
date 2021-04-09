import time
from datetime import datetime as dt
​
"""A list of the websites to be blocked"""
sites_to_block = [
    'www.facebook.com',  'facebook.com',
]
​
"""Different operating system host file location where we are going to add a list 
of websites we want to block"""

Linux_host = '/etc/hosts'
MacOs_host = '/private/etc/hosts'
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host
redirect = "127.0.0.1"

"""Defining two time intervals other than now"""
start_time =dt(dt.now().year,dt.now().month,dt.now().day,start_hour)
end_time =dt(dt.now().year,dt.now().month, dt.now().day,end_hour)
​
def block_websites(start_hour , end_hour):
    while True:
        if start_time < dt.now() < end_time: 
            print("It is working TIME !")
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in  sites_to_block:
                    if site not in hosts:
                       hostfile.write(redirect+' '+site+'\n')

        else:
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print('Enjoy your Social Media TIME !')
        time.sleep(3)

"""The function receives two-parameter, starting time end time"""
if __name__ == '__main__':
    block_websites(8, 18)








