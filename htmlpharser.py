# Description: This program takes a URL as input and displays the HTML content of the website.
import requests
from bs4 import BeautifulSoup

def display_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

website_url = input("Enter the website URL: ")
display_website(website_url)