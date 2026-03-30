from flask import Flask, render_template, request

app = Flask(__name__)

DEFAULTS = {
    "receipt_number": "IN0001",
    "receipt_date": "01-01-2025",
    "customer_name": "Jane Doe",
    "customer_address": "Flat 101,\nSample Residency, Sample Nagar,\nPune, Maharashtra,\n411001, India",
    "account_number": "10000000001",
    "company": "SAMPLE BROADBAND\n(SAMPLE TELECOM PVT LTD)",
    "gstin": "GSTIN 27AABCS1234C1ZX",
    "company_address": "Sample Nagar, Pune,\nMaharashtra, 411001, India",
    "billing_cycle": "Monthly",
    "payment_method": "Cash",
    "plan_speed": "100Mbps",
    "plan_package": "Unlimited",
    "plan_validity": "Monthly",
    "plan_amount": "1178.82",
    "favour_text": "SAMPLE BROADBAND (SAMPLE TELECOM PVT LTD) GSTIN 27AABCS1234C1ZX",
}


@app.route("/")
def index():
    return render_template("form.html", defaults=DEFAULTS)


@app.route("/generate", methods=["POST"])
def generate():
    bill = {key: request.form.get(key, "") for key in DEFAULTS}
    return render_template("invoice.html", bill=bill)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
