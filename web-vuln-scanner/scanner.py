import nmap
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ---------- 1. Port Scanner ----------
def port_scan(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(target, '1-1024', arguments='-T4 -F')
        results = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    results.append(f"[PORT] {port}/{proto} - {state}")
        return results
    except:
        return ["[!] Port scan failed"]

# ---------- 2. Subdomain Finder ----------
def subdomain_scan(domain):
    subdomains = ["www", "mail", "blog", "admin", "test", "dev", "shop", "portal"]
    found = []
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400:
                found.append(f"[SUBDOMAIN] {sub}.{domain} - Active")
        except:
            pass
    return found if found else ["[!] No subdomains found"]

# ---------- 3. Directory Bruteforce ----------
def dir_bruteforce(base_url):
    dirs = ["admin", "login", "dashboard", "uploads", "backup", "portal"]
    found = []
    for d in dirs:
        url = urljoin(base_url, d)
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                found.append(f"[DIR] {url} - Found")
        except:
            pass
    return found if found else ["[!] No hidden directories found"]
