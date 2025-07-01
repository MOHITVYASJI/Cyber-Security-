# 📡 Task 5: Capture and Analyze Network Traffic Using Wireshark

## 🎯 Objective

To capture live network traffic using *Wireshark*, identify different protocols, and observe how data flows in real time — especially focusing on unencrypted protocols like HTTP.

---

## 🛠 Tools Used

- 🐬 *Wireshark* – For packet sniffing and network traffic analysis
- 💻 Browser and basic internet activity – To generate live packets
- 📁 .pcap file – Saved packet capture for later analysis

---

## 📋 Steps Performed

1. Installed *Wireshark* on my system.
2. Selected the active network interface (e.g., Ethernet, Wi-Fi).
3. Started packet capture while browsing the web and performing test logins.
4. Applied filters like http, tcp, dns to analyze specific traffic.
5. Stopped capture and exported the .pcap file.
6. Analyzed captured packets for:
   - Protocol types
   - IP/Port info
   - Presence of clear-text credentials in HTTP packets
7. Wrote a detailed analysis report based on the capture.

---

## 🔍 Protocols Identified

- *HTTP* – Plaintext web communication
- *TCP* – Reliable transport layer protocol
- *DNS* – Domain name resolution
- *UDP* – Lightweight, fast connectionless communication

---

## 🔐 Security Insight

During testing, I accessed a demo *HTTP login page*, entered sample credentials, and noticed that:
- *Username and password were clearly visible in captured packets.*
- This confirms how risky it is to use *HTTP* instead of *HTTPS*.

⚠ This was done in a *safe, isolated, and ethical environment* for learning only.

---

## 📁 Files in this Repo

❌network_capture.pcap – Packet capture file
- analysis.md – Detailed protocol and vulnerability insights
- README.md – This documentation

---

## 📚 Key Learnings

- Wireshark can easily capture sensitive info over unsecured protocols.
- Encrypted protocols like HTTPS prevent such leaks.
- Using filters makes packet analysis efficient.
- Understanding protocols is essential for cyber security and troubleshooting.

---

> ✅ *Task Completed Successfully!*  
> 🧠 Skill Gained: Packet analysis, protocol identification, security awareness.

---

## 📸 Screenshots
Screenshots of filtered packets, login info in plain text, or protocol summaries.

---

## ⚖ Disclaimer

This project was done *strictly for educational purposes*. No real systems, users, or credentials were harmed or accessed.  
Always use such tools responsibly and ethically.
