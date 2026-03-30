# AutoBill

A web app that generates ISP internet invoices as printable PDFs, matching the layout of a standard broadband bill.

## Features

- Pre-filled form with all bill fields editable
- Invoice preview matching a real ISP bill layout
- Print to PDF via browser (Cmd+P / Ctrl+P → Save as PDF)

## GitHub Pages (no install needed)

1. Push the repo to GitHub
2. Go to **Settings → Pages → Source** and select your branch / root
3. Open the published URL — works entirely in the browser, no server required

## Run locally (static, no install)

Just open `index.html` in any browser:

```bash
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

Or serve it with Python:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Run with Flask

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5001
```

## Run with Docker

```bash
docker build -t autobill .
docker run -p 8080:8080 autobill
# → http://localhost:8080
```

## Project structure

```
autobill/
├── index.html              # Static version (GitHub Pages / open directly)
├── static/
│   ├── style.css           # Invoice + form styles
│   └── logo.jpg            # ISP logo
├── app.py                  # Flask server (alternative to static version)
├── templates/
│   ├── form.html
│   └── invoice.html
├── requirements.txt
└── Dockerfile
```

## Customising the logo

Replace `static/logo.jpg` with your own ISP logo. Adjust `.logo-img-crop` dimensions in `static/style.css` if the cropping needs tweaking.
