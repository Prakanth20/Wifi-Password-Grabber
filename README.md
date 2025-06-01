# Wi-Fi Password Grabber

A simple Python script to retrieve saved Wi-Fi SSIDs and their corresponding passwords from a Windows machine using the `netsh` command.

## 🔒 Disclaimer

This tool is for **educational purposes only**. Use it **only on systems you own** or have **explicit permission** to access. Unauthorized use may violate local or national laws.

---

## ⚙️ Features

* Lists all saved Wi-Fi SSIDs.
* Extracts and displays their corresponding passwords (if available).
* Simple, lightweight, and does not require external libraries.

---

## 🖥️ Requirements

* Python 3.x
* Windows OS

> This script uses `netsh`, a Windows command-line utility, and **will not work on macOS or Linux**.

---

## 🚀 Usage

1. **Clone or download this repository.**

2. **Run the script:**

   ```bash
   python wifi_password_grabber.py
   ```

3. **Output:**

   ```
   SSID: MyHomeWiFi, Password: mypassword123
   SSID: CoffeeShopWiFi, Password: N/A
   ```

---

## 🧠 How It Works

* It calls `netsh wlan show profiles` to list all saved Wi-Fi profiles.
* Then, for each profile, it runs `netsh wlan show profile name="SSID" key=clear` to retrieve stored passwords.
* Parses and displays the SSID and associated password (if found).

---

## 📁 Example Output

```plaintext
SSID: HomeNetwork, Password: supersecure123
SSID: OfficeNet, Password: N/A
SSID: GuestWiFi, Password: guest2024
```

---

## 🛑 Legal Notice

This script is intended **solely for legitimate uses** such as:

* Recovering your own Wi-Fi passwords.
* Network administration and audits.
* Educational or training purposes.

**Never use this tool to access or gather information from devices/networks without permission.**

---
