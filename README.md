<div align="center">

# 📱 PhoneNumberScanner

**Phone number information gathering tool — carrier, region, geolocation & more.**

*Built for OSINT research and educational purposes only.*

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Hexamora/PhoneNumberScanner)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Educational](https://img.shields.io/badge/Purpose-Educational-orange?style=for-the-badge)](#)

</div>

---

## 📖 About

**PhoneNumberScanner** is a Python-based CLI tool for gathering publicly available information from a phone number. It validates, parses, and enriches phone number data — from carrier and region detection to precise geolocation — making it useful for OSINT research, digital forensics, and investigative purposes.

---

## ✨ Features

- ✅ **Validation & Parsing** — validates phone numbers using the `phonenumbers` library
- 🌍 **Country & Region Detection** — identifies the country and region of origin
- 📡 **Carrier / Operator Lookup** — retrieves the telecom provider
- 🕐 **Timezone Detection** — shows associated timezones
- 📋 **Format Output** — displays both international and national formats
- 📍 **Geolocation** — uses `geopy` + Nominatim to get latitude, longitude & city
- 🔁 **Interactive CLI** — prompts for input and allows repeated scans without restarting

---

## 🖥️ Preview

```
╔══════════════════════════════════╗
║       PhoneNumberScanner         ║
╚══════════════════════════════════╝

[?] Enter phone number (e.g. +628123456789): +628123456789

[✓] Valid Number      : True
[+] Country           : Indonesia
[+] Region            : West Java
[+] Carrier           : Telkomsel
[+] International     : +62 812-3456-789
[+] National          : 0812-3456-789
[+] Timezone          : Asia/Jakarta
[+] Latitude          : -6.2088
[+] Longitude         : 106.8456
[+] City              : Jakarta
```

---

## 🚀 Installation & Usage

### Requirements

- Python 3.x
- pip

### Install & Run

```bash
# Install dependencies
pip install phonenumbers geopy requests

# Clone the repository
git clone https://github.com/Hexamora/PhoneNumberScanner.git

# Navigate to the directory
cd PhoneNumberScanner

# Run the script
python PhoneNumberScanner.py
```

### Input Format

```bash
# Always use international format with country code
+628123456789    # Indonesia
+14155552671     # United States
+447911123456    # United Kingdom
```

---

## 🧰 Tech Stack

| Library | Role |
|---|---|
| `phonenumbers` | Phone number validation, parsing & carrier lookup |
| `geopy` | Geolocation via Nominatim service |
| `requests` | HTTP requests |

---

## 📁 Project Structure

```
PhoneNumberScanner/
├── PhoneNumberScanner.py   # Main script
└── README.md
```

---

## ⚠️ Legal Disclaimer

> **PhoneNumberScanner** is intended **strictly for educational purposes, OSINT research, and digital forensics on information you are legally authorized to access.**
>
> This tool only retrieves **publicly available** information. Misuse of this tool may violate privacy laws and regulations in your country. The author is **not responsible** for any misuse or illegal activity conducted with this tool.

---

## 👤 Author

**Hexamora** — [@Hexamora](https://github.com/Hexamora)

---

<div align="center">

*Use responsibly. For educational and research purposes only.*

⭐ **Star this repo if you find it useful!**

</div>
