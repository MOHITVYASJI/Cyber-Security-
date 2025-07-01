# 🕵‍♂ Network Traffic Analysis using Wireshark

## 🔍 Overview

In this task, I used *Wireshark* to capture and analyze real-time network traffic on my system. The objective was to observe how network protocols work and how sensitive information can travel over a network — especially when encryption is not used.

## 🛠 Tools Used

- *Wireshark* (Packet sniffer and network analyzer)
- Local browser & internet activity to generate network traffic

---

## 🎯 Steps Performed

1. Launched *Wireshark* and selected my active network interface.
2. Started live packet capture.
3. Generated traffic by:
   - Visiting HTTP-based websites (for learning only)
   - Performing login/signup on a *test/demo HTTP site*
4. Applied *Wireshark filters* like:
   - http
   - tcp
   - dns
5. Captured traffic for ~1 minute and saved as .pcap file.

---

## 📡 Protocols Identified

During the capture, the following protocols were observed:
- *HTTP* – Web requests (unencrypted)
- *TCP* – Connection-oriented transport protocol
- *DNS* – Domain name resolution
- *UDP* – For fast, connectionless traffic (seen in some requests)

---

## 🔐 Security Insight: Capturing Login Credentials (Test-Only)

> ⚠ This was done on a *non-sensitive test website* to demonstrate vulnerabilities in HTTP.

- When login/signup was performed over *HTTP, the **username and password were clearly visible* in plain text.
- This highlights why *HTTPS* is essential — without it, attackers on the same network can intercept credentials using tools like Wireshark.

---


## 📚 Key Learnings

- Network packets can reveal sensitive info if encryption is not used.
- Tools like Wireshark help visualize and inspect real-time traffic.
- Protocol filtering makes analysis more efficient.
- Basic cyber hygiene like *avoiding HTTP logins* is crucial for safety.

---

> 🛡 *Ethical Note:*  
> All actions were performed in a *safe, legal, and controlled environment* for learning purposes only. No real-world websites or unauthorized systems were tested.
