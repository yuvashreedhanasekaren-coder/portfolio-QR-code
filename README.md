# Portfolio QR Generator

An AI-powered Python project that generates a QR code for a portfolio website and analyzes the portfolio content using a local AI model.

## Project Overview

Portfolio QR Generator combines **Python, web scraping, QR code generation, Flask, and local AI**.

The application:

1. Fetches the portfolio website content.
2. Extracts useful portfolio information.
3. Analyzes the content using a local AI model through Ollama.
4. Generates a QR code for the portfolio.
5. Displays the QR code and AI analysis through a Flask web dashboard.

## Portfolio QR Code

Scan the QR code below to open the portfolio website.

![Portfolio QR Code](static/portfolio_qr.png)

**Scan the QR code with your phone camera to open the portfolio.**

## Current Status

**Development Status: In Progress**

### Completed

- [x] Python project setup
- [x] Portfolio URL configuration
- [x] QR code generation
- [x] Portfolio website content extraction
- [x] HTML content cleaning and text extraction
- [x] AI analysis prompt preparation
- [x] Local AI integration code
- [x] Flask web application
- [x] Flask dashboard
- [x] QR code display
- [x] AI analysis display
- [x] AI analysis error handling
- [x] QR code verification
- [x] GitHub repository setup
- [x] Project documentation

### Currently Working On

- [ ] Ollama local AI model setup

### Next Steps

- [ ] Real AI portfolio analysis
- [ ] Final end-to-end testing
- [ ] Deployment

## Technologies

- Python
- Flask
- BeautifulSoup
- Requests
- QRCode
- Ollama
- Local AI Model
- HTML / CSS
- Git / GitHub

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
├── README.md
│
├── static/
│   └── portfolio_qr.png
│
└── templates/
    └── index.html
````

## How It Works

```text
Portfolio URL
      ↓
Python Web Scraper
      ↓
Portfolio Content Extraction
      ↓
Ollama Local AI
      ↓
AI Portfolio Analysis
      ↓
QR Code Generation
      ↓
Flask Web Dashboard
      ↓
QR Code + AI Analysis
```

## AI Analysis

The project uses a local AI model through Ollama to analyze the portfolio content.

The AI analysis is designed to identify:

* Professional category
* Technical skills
* Main areas of interest
* Portfolio information
* Short portfolio summary

The AI integration is implemented locally without depending on a paid cloud AI API.

**Current status:** Ollama is installed and the AI integration code is completed. The local AI model setup is the current remaining task.

## QR Code

The QR code is generated from the portfolio URL configured in `config.py`.

The generated QR code is stored in:

```text
static/portfolio_qr.png
```

Scanning the QR code opens the configured portfolio website directly.

## Flask Web Dashboard

The Flask application provides a web dashboard that displays:

* Portfolio title
* Generated QR code
* AI portfolio analysis

The dashboard also handles AI analysis errors when the local AI service or model is unavailable.

## Development Timeline

The project is currently in the final AI model setup and testing stage.

## Planned Final Workflow

```text
Run the application
        ↓
Fetch portfolio
        ↓
Extract portfolio content
        ↓
Analyze portfolio using local AI
        ↓
Generate QR code
        ↓
Display results in web dashboard
        ↓
Verify complete workflow
        ↓
Deploy application
```

## Project Goal

The goal is to build a practical **AI-powered portfolio QR generator** that combines portfolio analysis and QR-based portfolio sharing in a single Python application.
