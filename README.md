# Portfolio QR Generator

An AI-powered Python project that automatically generates a QR code for a portfolio website and analyzes the portfolio content using a local AI model.

## Project Overview

Portfolio QR Generator combines **Python, web scraping, QR code generation, Flask, and local AI** to create a simple portfolio-sharing and analysis system.

The portfolio URL is configured directly in the project. When the application is completed, it will:

1. Fetch the portfolio website content.
2. Extract useful portfolio information.
3. Analyze the content using a local AI model through Ollama.
4. Generate a QR code for the portfolio.
5. Display the QR code and AI-generated portfolio analysis through a web page.

## Current Status

**Development Status: In Progress**

### Completed

- [x] Python project setup
- [x] Portfolio URL configuration
- [x] QR code generation
- [x] Portfolio website content extraction
- [x] HTML content cleaning and text extraction
- [x] AI analysis prompt preparation
- [x] GitHub repository setup

### Currently Working On

- [ ] Ollama local AI setup
- [ ] Local AI portfolio analysis
- [ ] AI-generated portfolio report
- [ ] Flask web application
- [ ] Web dashboard
- [ ] QR code display
- [ ] AI analysis display
- [ ] QR verification
- [ ] Error handling and validation
- [ ] Final UI improvements
- [ ] Final testing and documentation

## Technologies

- Python
- Flask
- BeautifulSoup
- Requests
- QRCode
- Ollama
- Local AI Model
- HTML / CSS

## Project Structure

```text
portfolio-QR-generator/
│
├── app.py
├── config.py
├── ai_analyzer.py
├── qr_generator.py
├── requirements.txt
├── .gitignore
│
├── generated_qr/
│   └── portfolio_qr.png
│
└── README.md
````

## How It Works

```text
Portfolio URL
      ↓
Python Web Scraper
      ↓
Portfolio Content
      ↓
Ollama Local AI
      ↓
AI Portfolio Analysis
      ↓
QR Code Generation
      ↓
Flask Web Dashboard
```

## AI Analysis

The project uses a local AI model through Ollama to analyze the portfolio content.

The AI analysis is designed to identify information such as:

* Professional category
* Technical skills
* Main areas of interest
* Portfolio projects
* Short portfolio summary

The AI runs locally instead of depending on a paid cloud API.

## QR Code

The project generates a QR code from the configured portfolio URL.

Scanning the generated QR code opens the portfolio website directly.

## Development Timeline

The project is being developed step-by-step using meaningful Git commits.

**Current Progress:**

* Commit 1 — Initial project setup ✅
* Commit 2 — Portfolio URL configuration ✅
* Commit 3 — QR code generation ✅
* Commit 4 — Portfolio content analyzer ✅
* Commit 5 — Local AI integration 🔄

**Estimated remaining development time:**

Approximately **2–4 days**, depending on testing and UI refinement.

The goal is to complete the functional version first and then perform final testing, documentation, and cleanup.

## Planned Final Workflow

Once development is complete:

```text
Run the application
        ↓
Fetch portfolio
        ↓
Analyze portfolio using local AI
        ↓
Generate QR code
        ↓
Display results in web dashboard
```

## Project Goal

The goal is to build a practical **AI-powered portfolio QR generator** that combines portfolio analysis and QR-based portfolio sharing in a single Python application.
