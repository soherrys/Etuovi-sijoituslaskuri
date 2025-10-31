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
- **Web Scraping**: Selenium WebDriver + Chromium (headless)
- **Frontend**: HTML + CSS (Jinja2 templates)
- **Data Parsing**: JSON extraction from JavaScript state

## Configuration
The application is configured for the Replit environment:
- Binds to `0.0.0.0:5000` for web preview
- Cache-Control headers prevent iframe caching issues
- Debug mode controlled via `FLASK_DEBUG` environment variable
- Port configurable via `PORT` environment variable (defaults to 5000)

## Recent Changes
- **2025-10-31**: Upgraded to Selenium-based scraping
  - Replaced requests+BeautifulSoup with Selenium WebDriver
  - Installed Chromium browser and ChromeDriver for headless scraping
  - Updated scraper to extract data from JavaScript state (window.__INITIAL_STATE__)
  - Successfully scraping 30+ properties from etuovi.com
  
- **2025-10-31**: Initial setup for Replit environment
  - Renamed files to lowercase for Python import compatibility
  - Moved static folder to root directory (Flask standard structure)
  - Added cache-busting headers for Replit's iframe proxy
  - Configured Flask to bind to 0.0.0.0:5000
  - Set up deployment configuration for autoscale
  - Added .gitignore for Python project

## How It Works
1. Selenium WebDriver (headless Chrome) loads the etuovi.com search page
2. JavaScript state data is extracted from `window.__INITIAL_STATE__`
3. Property listings are parsed from the JSON structure
4. For each property, the calculator computes:
   - Rental yield percentage (annual rent / purchase price)
   - Monthly cash flow (rent - maintenance fees - loan payment)
   - ROI based on 30% down payment
5. Results are displayed in a clean web interface

## Performance Note
The first page load takes 5-10 seconds as Selenium starts a headless Chrome browser to scrape the data. Subsequent loads will be equally slow since the data is fetched fresh on each request. For production use, consider caching the results or using a background task to update data periodically.
