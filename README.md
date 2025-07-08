
### Web Scraping Notes: Housing Price Data using Selenium

This repository documents a complete hands-on project for scraping real estate listings using Selenium in Python, cleaning the scraped data, and saving it for further analysis or machine learning tasks.
Unlike using pre-made datasets from platforms like Kaggle, this project involves building your own dataset from scratch, with real-time data scraped from Housing.com.

---

Tech Stack:

* Language: Python 3.x
* Web Driver: ChromeDriver
* Libraries: Selenium, Pandas, Time, OS, Jupyter Notebook

---

How to Use:

1. Clone the Repository
   git clone [https://github.com/harshavardhant2005/web-scrpaing-notes.git](https://github.com/harshavardhant2005/web-scrpaing-notes.git)
   cd web-scrpaing-notes

2. Set Up Environment
   pip install -r requirements.txt

   (Optional) If you're using a virtual environment, activate it inside the env/ folder.

3. Download ChromeDriver
   Make sure your Chrome browser version matches the ChromeDriver version from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   Place the driver inside the chromedriver/ folder.

4. Run the Scraper
   You can run the script via:
   python main.py

   or use the Jupyter notebook:
   jupyter notebook final\_scraper.ipynb

---

Dataset Overview:

* Raw Data: Saved in house\_price\_data.csv
* Cleaned Data: Saved in cleaned\_property\_data.csv
* Columns may include: Title, Price, Location, Area, BHK, Amenities, etc.
      
---

ML Use Case Ideas:

* Predict house prices using regression models
* Cluster similar listings based on location/features
* Build a recommendation system for property buyers

---

Notes & Good Practices:

* Scraping respects ethical boundaries — delays (time.sleep()) are used
* Avoid scraping too frequently to prevent IP bans
* Always check the website’s robots.txt

