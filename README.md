# TOMAS-LOGINFINDER
# TOMAS-LOGINFINDER ًں”چ

A powerful Python-based tool to scan websites for hidden or common login/admin panels using a wordlist.  
Perfect for ethical hackers, CTF players, and cybersecurity learners.

---

## ًںژ¯ Features

- ًں”ژ Fast and reliable scanner for admin/login panels
- ًں“‚ Custom wordlist support (`common.txt`)
- ًںژ¨ Colored terminal output without external libraries
- ًں’» Works on **Termux**, **Kali Linux**, or any Python3 system

---

## âڑ™ï¸ڈ Requirements

- Python 3.x
- requests module

Install dependencies:

```bash
pip install requests
```

---

## ًں“¥ Installation

```bash
# Clone the tool from GitHub
git clone https://github.com/Toma1264git0hub/TOMAS-LOGINFINDER.git

# Enter the project directory
cd TOMAS-LOGINFINDER

# List the contents to verify
ls
# â‍¤ loginhunt.py  common.txt

# Run the tool
python loginhunt.py
```

---

## ًںڑ€ How to Use

1. Make sure `common.txt` and `loginhunt.py` are in the same folder.
2. Run the tool:
   ```bash
   python loginhunt.py
   ```
3. You will be prompted:
   ```
   [?] Enter website URL (e.g. https://example.com):
   ```
   Enter the full target website URL (with http or https).

4. The tool scans for common paths:
   ```
   /admin
   /login
   /cpanel
   /dashboard
   /admin-panel
   ...
   ```

5. Example output:
   ```
   [+] Found hidden page: http://example.com/admin
   [-] Not found: http://example.com/loginpanel
   ```

---

## ًں“پ Project Structure

```
TOMAS-LOGINFINDER/
â”œâ”€â”€ loginhunt.py      â†گ Main scanning script
â””â”€â”€ common.txt        â†گ Wordlist of login/admin paths
```

You can edit `common.txt` and add custom paths.

---

## ًں“، Connect With Me

- **Telegram:** [@K_DKP](https://t.me/K_DKP)
- **GitHub:** [@toma1264git0hub](https://github.com/toma1264git0hub)
- **TikTok:** [@.html.1](https://www.tiktok.com/@.html.1)

---

## âڑ ï¸ڈ Disclaimer

> This tool is for **educational purposes only**.  
> Do **NOT** use it against websites without **permission**.  
> The developer is **not responsible** for any misuse or illegal activity.
