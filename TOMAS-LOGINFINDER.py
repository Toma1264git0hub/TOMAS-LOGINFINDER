import requests
#Please do not change the rights. 
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

print(f"""{RED}
TTTTTTT   {YELLOW}OOOOO   {GREEN}M     M   {CYAN}AAAAA   {RED}SSSSS
   {RED}T     {YELLOW}O     O  {GREEN}MM   MM  {CYAN}A     A  {RED}S
   {RED}T     {YELLOW}O     O  {GREEN}M M M M  {CYAN}AAAAAAA   {RED}SSS
   {RED}T     {YELLOW}O     O  {GREEN}M  M  M  {CYAN}A     A      {RED}S
   {RED}T      {YELLOW}OOOOO   {GREEN}M     M  {CYAN}A     A  {RED}SSSSS
{RESET}""")

print(f"{CYAN}TELEGRAM:@K_DKP")
print(f"GITHUB:@toma1264git0hub")
print(f"TIKTOK:@.html.1{RESET}\n")
print(f"{RED}TOMAS-LOGINFINDER TOOL")

site = input(f"{YELLOW}[?] Enter website URL (e.g. https://example.com): {RESET}")

try:
    with open("common.txt", "r") as f:
        paths = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"{RED}[!] File 'common.txt' not found!{RESET}")
    exit()

print(f"\n{CYAN}[*] Starting login page scan using common.txt...{RESET}\n")

for path in paths:
    url = site.rstrip("/") + "/" + path
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in [200, 301, 302]:
            print(f"{GREEN}[+] Found possible login page: {url}{RESET}")
        else:
            print(f"{RED}[-] Not found: {url} ({response.status_code}){RESET}")
    except requests.RequestException:
        print(f"{RED}[-] Error connecting to: {url}{RESET}")