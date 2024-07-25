

# To automate routine web scraping tasks, you can use Python to scrape data periodically and save the results to a file or a database. Here's a step-by-step guide using requests, BeautifulSoup, and schedule libraries to scrape a website daily and save the data to a CSV file.




import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time


url = 'https://example-news-website.com'

def scrape_and_save():
 
    response = requests.get(url)

  
    if response.status_code == 200:
      
        soup = BeautifulSoup(response.content, 'html.parser')

    
        titles = soup.find_all('h2', class_='title')

       
        titles_list = [title.get_text() for title in titles]

       
        df = pd.DataFrame(titles_list, columns=['Title'])

   
        current_date = pd.Timestamp.now().strftime('%Y-%m-%d')
        df.to_csv(f'news_titles_{current_date}.csv', index=False)
        print(f"Data saved for {current_date}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


schedule.every().day.at("10:00").do(scrape_and_save)


while True:
    schedule.run_pending()
    time.sleep(1)
