# Portfolio QR Generator

An AI-powered Python project that automatically generates a QR code for a portfolio website and analyzes the portfolio content using a local AI model.

## Project Overview

Portfolio QR Generator combines **Python, web scraping, QR code generation, Flask, and local AI** to create a portfolio-sharing and analysis system.

The portfolio URL is configured directly in the project.

The application is designed to:

1. Fetch the portfolio website content.
2. Extract useful portfolio information.
3. Analyze the content using a local AI model through Ollama.
4. Generate a QR code for the portfolio.
5. Display the QR code and AI-generated portfolio analysis through a web dashboard.

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

### Currently Working On

- [ ] Ollama local AI model setup
- [ ] Real AI portfolio analysis
- [ ] Final end-to-end testing
- [ ] Final documentation
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

The AI analysis is designed to identify information such as:

* Professional category
* Technical skills
* Main areas of interest
* Portfolio information
* Short portfolio summary

The AI integration is implemented locally so that the project does not depend on a paid cloud AI API.

**Note:** The Ollama integration code is completed, but the local AI model setup and real AI analysis testing are part of the remaining development.

## QR Code

The project generates a QR code from the configured portfolio URL.

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

The dashboard also handles AI analysis errors gracefully when the local AI service is unavailable.

## Development Timeline

The project is being developed step-by-step using meaningful Git commits.

### Current Progress

* Commit 1 — Initial project setup
* Commit 2 — Portfolio URL configuration
* Commit 3 — QR code generation
* Commit 4 — Portfolio content analyzer
* Commit 5 — Local AI integration
* Commit 6 — AI analyzer improvements
* Commit 7 — Flask integration
* Commit 8 — Flask application setup
* Commit 9 — Dashboard development
* Commit 10 — Flask dependency setup
* Commit 11 — Improve QR code generation reliability
* Commit 12 — Optimize QR handling in Flask app
* Commit 13 — Improve AI analysis display

The project is currently in the development and testing stage.

## Planned Final Workflow

Once development is complete:

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
