# 🔥 Task 4: Setup and Use a Firewall on Linux (UFW)

## 🎯 Objective:
Configure and test basic firewall rules to allow or block traffic using UFW (Uncomplicated Firewall) on Linux (Kali).

---

## 🧰 Tools Used:
- **UFW (Uncomplicated Firewall)** – A simple command-line firewall tool for managing iptables.
- **Linux Terminal** – For executing commands.
- **Nmap (optional)** – For testing open/closed ports.

---

## 🪜 Steps Followed:

### 🛠️ 1. Installed UFW (If not already installed)
```bash
sudo apt update
sudo apt install ufw -y
🔐 2. Enabled the Firewall
bash
sudo ufw enable
📊 3. Checked the Default Status & Rules
```bash
sudo ufw status verbose
🚫 4. Blocked Inbound Traffic on Port 23 (Telnet)
```bash
sudo ufw deny 23
✅ This helps prevent Telnet-based attacks, as Telnet is insecure and outdated.

✅ 5. Allowed SSH (Port 22) for Secure Access
```bash
sudo ufw allow 22
🧪 6. Tested Rules using nmap (optional)
```bash
nmap -p 23,22 127.0.0.1
🧹 7. Removed the Test Rule (Optional)
```bash
sudo ufw delete deny 23
📝 8. Exported Current Rules to File
```bash
sudo ufw status verbose > ufw_rules.txt

📁 Files Included:
File Name	Description
README.md	This documentation file
ufw_rules.txt	Output of the active firewall rules (status)

🧠 Summary – What Is a Firewall?

A firewall is a security system that monitors and filters incoming and outgoing network traffic. It works based on predefined rules to block or allow traffic to specific ports and services.
Inbound rules: Manage traffic coming into your device.
Outbound rules: Manage traffic going out of your device.
Port: A logical endpoint for network communication (e.g., port 22 for SSH, port 80 for HTTP).

✅ Outcome:
I successfully configured UFW on my Kali Linux machine, tested inbound rules, allowed safe connections (like SSH), and blocked unsafe ports (like Telnet).
This task enhanced my understanding of basic firewall configurations and how network traffic can be filtered for better security.
