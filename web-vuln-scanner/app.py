from flask import Flask, render_template, request
from scanner import port_scan, subdomain_scan, dir_bruteforce

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        target = request.form.get("url")
        if target:
            # Run all scans
            findings = []
            findings.append("\n--- PORT SCAN ---")
            findings.extend(port_scan(target))
            findings.append("\n--- SUBDOMAIN SCAN ---")
            domain = target.replace("http://", "").replace("https://", "").split("/")[0]
            findings.extend(subdomain_scan(domain))
            findings.append("\n--- DIRECTORY BRUTEFORCE ---")
            findings.extend(dir_bruteforce(target))
            results = findings
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
