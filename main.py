# main.py
"""
Entry point that wires driver + scraper, matching original 'if __name__ == "__main__"' flow.
This file mirrors your original example usage.
"""
import time
import random
from .driver import init_stealth_driver
from .scraper import search_places, scroll_sidebar_to_end, loop_all_listings_and_scrape_data

def run_demo():
    driver = None
    try:
        driver = init_stealth_driver(headless=False)

        driver.get("https://www.google.com/maps")
        time.sleep(random.uniform(8, 10))

        search_places(driver, "churches in faisalabad")
        time.sleep(random.uniform(8, 10))

        scroll_sidebar_to_end(driver, (4, 6))

        loop_all_listings_and_scrape_data(driver)

        print("Page title:", driver.title)
        time.sleep(random.uniform(2, 4))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass
            driver = None  # Prevent __del__ double quit

if __name__ == "__main__":
    run_demo()
