from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.faz.net/aktuell/', timeout=600).text
html_text = BeautifulSoup(html_text, 'lxml')


