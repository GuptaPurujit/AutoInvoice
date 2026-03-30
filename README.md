# WiFi Bill Generator

A local web app that generates ISP internet invoices as printable PDFs, matching the layout of a standard broadband bill.

## Features

- Pre-filled form with all bill fields editable
- Live invoice preview matching a real ISP bill layout
- Print to PDF via browser (Cmd+P / Ctrl+P → Save as PDF)

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5001, fill in the details, click **Generate Invoice**, then **Print / Save as PDF**.

## Run with Docker

```bash
docker build -t wifi-bill-generator .
docker run -p 8080:8080 wifi-bill-generator
```

Open http://localhost:8080.

## Project structure

```
wifi_bill_generator/
├── app.py                  # Flask server (two routes: form + invoice)
├── requirements.txt
├── Dockerfile
├── static/
│   ├── style.css           # Invoice + form styles
│   └── logo.jpg            # ISP logo
└── templates/
    ├── form.html           # Bill input form
    └── invoice.html        # Printable invoice layout
```

## Customising the logo

Replace `static/logo.jpg` with your own ISP logo. The image is cropped to show only the top portion — adjust `.logo-img-crop` dimensions in `style.css` if needed.
