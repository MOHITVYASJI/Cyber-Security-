# ✅ Task 1 - Port Scanning Analysis

## 🔍 Scanned IP Range:
10.0.2.0/24

## ✅ Hosts Found:
- *10.0.2.2*  
  Open Ports:  
  - 135 (msrpc)  
  - 445 (microsoft-ds)  
  - 2179 (vmrdp)  
  - 3306 (mysql)

- *10.0.2.3*  
  All ports filtered

- *10.0.2.15 (self)*  
  All ports closed ✅

---

## ⚠ Risks:
- MySQL & SMB open hone se data leak ya remote access ho sakta hai
- RPC port bhi vulnerable hota hai if not secured
- 10.0.2.3 pe firewall laga ho sakta hai, par completely invisible bhi ho sakta hai

---

## 🔐 Security Suggestions:
- Close unused ports
- Use strong passwords for services like MySQL
- Apply firewall (e.g., ufw, iptables)
- Keep systems updated

> Scan kiya gaya sirf educational virtual network par — no external IP involved.
