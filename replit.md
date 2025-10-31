# Sijoitusasunnot Kajaanissa (Investment Properties in Kajaani)

## Overview
A Flask web application that scrapes property listings from a Finnish real estate website (etuovi.com) and calculates investment returns for apartments in Kajaani, Finland. The app displays rental yield (vuokratuotto), cash flow (kassavirta), and ROI calculations for each property.

## Project Structure
- `main.py` - Flask application entry point with route definitions and caching configuration
- `scraper.py` - Web scraper that fetches property listings from etuovi.com
- `calculator.py` - Investment calculation logic for rental properties
- `templates/index.html` - HTML template for displaying property listings
- `static/style.css` - CSS styling for the web interface
- `requirements.txt` - Python dependencies (Flask, requests, beautifulsoup4)

## Technology Stack
- **Backend**: Flask (Python 3.11)
- **Web Scraping**: BeautifulSoup4 + Requests
- **Frontend**: HTML + CSS (Jinja2 templates)

## Configuration
The application is configured for the Replit environment:
- Binds to `0.0.0.0:5000` for web preview
- Cache-Control headers prevent iframe caching issues
- Debug mode controlled via `FLASK_DEBUG` environment variable
- Port configurable via `PORT` environment variable (defaults to 5000)

## Recent Changes
- **2025-10-31**: Initial setup for Replit environment
  - Renamed files to lowercase for Python import compatibility
  - Moved static folder to root directory (Flask standard structure)
  - Added cache-busting headers for Replit's iframe proxy
  - Configured Flask to bind to 0.0.0.0:5000
  - Set up deployment configuration for autoscale
  - Added .gitignore for Python project

## How It Works
1. The scraper fetches apartment listings from etuovi.com for Kajaani city center
2. For each property, the calculator computes:
   - Rental yield percentage
   - Monthly cash flow (rent - maintenance fees - loan payment)
   - ROI based on 30% down payment
3. Results are displayed in a clean web interface

## Note
The web scraper targets a specific website structure which may change over time. If no properties appear, the website's HTML structure may have been updated and the scraper selectors would need to be adjusted.
