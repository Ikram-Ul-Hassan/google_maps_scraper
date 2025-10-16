# 🗺️ Google Maps Smart Scraper  
**Automate Google Maps data extraction with precision, stealth, and simplicity — built in Python & Selenium.**  

---

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Automation-Selenium-orange?style=for-the-badge&logo=selenium&logoColor=white" />
</p>

---

## 👨‍💻 Author & Maintainer  

**Developed & Maintained by:**  
> *Automation Engineer • Python Developer • Web Scraping Specialist*  
> *Passionate about turning data chaos into structured insight.*

---

### 🌐 Connect With Me
  
 - <a href="https://github.com/Ikram-Ul-Hassan" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" />
  </a>

 
 - <a href="https://www.linkedin.com/in/ikram-ul-hassan/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-%230A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  
 - <a href="https://www.kaggle.com/ikramshah512" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" />
  </a>

 
 - <a href="mailto:shahikram295@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>


---

### 🚀 Elevator Pitch  
Extract structured business data directly from **Google Maps** — automatically.  
Built with stealthy browser automation, human-like scrolling, and a clean modular architecture.

---


## 🌟 Key Features  

✅ **Automated Scrolling** – Loads every Google Maps listing dynamically.  
✅ **Human-Like Clicks** – Simulates natural browsing patterns for smooth performance.  
✅ **JSON Data Export** – Saves results like name, rating, address, phone, and website.  
✅ **Stealth Mode** – Avoids easy detection via browser fingerprints.  
✅ **Professional Modular Design** – Optimized for maintainability and privacy.

---

## 🧩 Project Overview  

This project is built on a **multi-file modular architecture** for better separation of concerns:

| File | Purpose |
|------|----------|
| `main.py` | Public entry point – orchestrates scraping flow |
| `driver.py` | Handles Chrome driver initialization (private) |
| `scraper.py` | Core scraping and data parsing logic (private) |
| `utils.py` | Helper methods: delays, safe clicks, and element management (private) |
| `requirements.txt` | Dependencies list |

---

### 🔒 Privacy & Repository Note  

> 💡 **Note from Author:**  
> For intellectual property and ethical scraping protection, **only `main.py` is publicly visible on GitHub**.  
> All other core modules (`driver.py`, `scraper.py`, `utils.py`) are **intentionally included in `.gitignore`** to protect proprietary techniques and prevent misuse.  
>  
> You can still fully understand the scraper’s behavior and workflow via the documented public interface in `main.py`.

This approach aligns with GitHub’s fair code-sharing practices and keeps sensitive browser automation logic secure.

---

## ⚙️ Setup & Installation  

### 1️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 2️⃣ Ensure ChromeDriver compatibility

Make sure your Chrome browser version matches the installed chromedriver.
If not, download the correct version here:
👉 https://chromedriver.chromium.org/downloads 

### 3️⃣ Run the scraper
```
python main.py

```

### 4️⃣ Output location

```
data.json

```

## 🧠 Example Use Case

```
# main.py
from driver import init_stealth_driver
from scraper import search_places, scroll_sidebar_to_end, loop_all_listings_and_scrape_data

driver = init_stealth_driver(headless=False)
driver.get("https://www.google.com/maps")

search_places(driver, "coffee shops in San Francisco")
scroll_sidebar_to_end(driver)
loop_all_listings_and_scrape_data(driver)

driver.quit()

```

## 🧾 Example Output
```
[
  {
    "title": "Blue Bottle Coffee",
    "rating": "4.6",
    "total_reviews": "1,245 reviews",
    "category": "Coffee shop",
    "address": "66 Mint St, San Francisco, CA",
    "phone": "+1 415-495-3399",
    "website": "https://www.bluebottlecoffee.com"
  }
]

```

## 🧩 Configuration Options
| Parameter                  | Description                         | Defined In   |
| -------------------------- | ----------------------------------- | ------------ |
| `headless`                 | Run in background mode (True/False) | `driver.py`  |
| `pause_between_scrolls`    | Adjust scrolling delay range        | `scraper.py` |
| `max_attempts_without_new` | Stop condition for scrolling        | `scraper.py` |
| `save_path`                | Output file path for JSON results   | `scraper.py` |


## 🌍 Why This Project Matters
Data fuels decisions — and local data is gold.
This tool transforms Google Maps business listings into structured, machine-readable datasets for analysis, marketing, or research.

### 💼 Use it to:

- Discover competitors or
- Find potential leads by area
- Map local business density for market insights
- Automate manual location-based research

### 👥 Who It’s For

- 👨‍💻 Data Researchers – Quickly build datasets of real-world businesses.
- 🏢 Startup Founders – Analyze local markets and competitors.
- 📊 Digital Marketers – Collect business info for targeted outreach and SEO.

### 💡 Demo Ideas

- 1️⃣ Scrape all coffee shops in a city and compare review averages.
- 2️⃣ Visualize business density using scraped addresses and coordinates.
- 3️⃣ Generate local lead lists (e.g., all restaurants with websites) in seconds.

### 🔐 Ethical Use & Security

⚠️ Please follow Google Maps Terms of Service
.
This scraper is for educational and personal research purposes only.
Avoid mass scraping or resale of data — this project is meant to empower learning and innovation, not abuse.

### 🧪 Developer Insights

- Main workflow resides in main.py for easy readability.
- Private modules handle internal browser logic securely.
- save_to_json ensures clean, readable output data.
- Fully modular — easily extendable for other data sources or search queries.

## 📦 Requirements
```
selenium>=4.0.0
fake-useragent
undetected-chromedriver
webdriver-manager
```

## License

**MIT License** — You’re free to modify, share, and use commercially.
Please credit the author when sharing publicly or deriving works.

## 💬 Spread the Word

If you find this project useful,
⭐ Star this repo, fork it, or share it on LinkedIn / Twitter using:
#GoogleMapsScraper #PythonAutomation

<p align="center"> Made with ❤️ by passionate developers who love clean automation. </p> ```


