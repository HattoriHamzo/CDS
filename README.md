<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Coffee Data Scraper</h3>

  <p align="center">
    A Scrapy-based web scraper to extract coffee information from a coffee website.
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Coffee Data Scraper is a web scraping project built using Scrapy, a powerful and flexible web scraping framework in Python. The scraper is designed to extract coffee-related information such as coffee name, price, and image from a coffee website. It navigates through the website's structure, selects specific HTML elements, and collects the desired data.

Here's why this project can be useful:
* Obtain coffee information from an online source without manual data entry.
* Automate the collection of coffee images, prices, and names for analysis.


<!-- BUILT WITH -->
### Built With

This project is built using the Scrapy framework, which is a powerful tool for web scraping in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


<!-- GETTING STARTED -->
## Getting Started

This section will guide you through setting up the Coffee Data Scraper on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:
* Python (3.6+)
* Scrapy

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/your_username/Coffee-Data-Scraper.git
   ```
2. Navigate to the project folder
   ```sh
   cd Coffee-Data-Scraper
   ```
3. Install poetry dependencies
   ```sh
   poetry install
   ```
4. Get the poetry executable to use the custom environment
   ```sh
   poetry env info
   ```
   You will see something like this:
   ```sh
   virtualenv
    Python:         3.11.4
    Implementation: CPython
    Path:           /Users/your_user/Library/Caches/pypoetry/virtualenvs/coffe-data-scraper-Wtgo2mew-py3.11
    Executable:     /Users/your_user/Library/Caches/pypoetry/virtualenvs/coffe-data-scraper-Wtgo2mew-py3.11/bin/python
    Valid:          True
    
    System
    Platform:   darwin
    OS:         posix
    Python:     3.11.4
    Path:       /usr/local/opt/python@3.11/Frameworks/Python.framework/Versions/3.11
    Executable: /usr/local/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/bin/python3.11
   ```
   Now copy and paste the "Executable":
   ```sh
   /Users/your_user/Library/Caches/pypoetry/virtualenvs/coffe-data-scraper-Wtgo2mew-py3.11/bin/python
   ```
   Change your Python interpreter un vscode with that executable path


6. You can launch the main.py file or use the .launch settings provided (you can just hit play on debug if you are using vscode)
