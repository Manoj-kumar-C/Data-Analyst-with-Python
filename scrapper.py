import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json

def scrape_youtube_channel(channel_url):
    # Initialize ChromeDriver (make sure you specify the path to your chromedriver executable)
    driver = webdriver.Chrome(executable_path='./chromedriver')

    # Load the channel URL
    driver.get(channel_url)

    # Parse the HTML content of the channel page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all elements with class "yt-lockup-title" which represent videos
    video_elements = soup.find_all(class_='yt-lockup-title')
    videos = []

    # Extract video ID and title from each video element
    for video_element in video_elements:
        video_link = video_element.find('a')
        video_id = video_link['href'].split('=')[-1]
        video_title = video_link['title']
        videos.append({'video_id': video_id, 'title': video_title})

    # Close the driver
    driver.quit()

    return videos

def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
channel_url = 'https://www.youtube.com/channel/UCQcnfU7cYxMiP9L1l-kRm_A'
channel_videos = scrape_youtube_channel(channel_url)
save_as_json(channel_videos, 'channel_videos.json')
