from bs4 import BeautifulSoup
import requests
from simple_chalk import chalk

# A script to scrap html elements content from hackernews using BeautifulSoup 4

# To bypass some of the website restrictions
header = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
url = 'https://news.ycombinator.com/news'
req = requests.get(url, header)

soup = BeautifulSoup(req.content, 'lxml')

# Select all elements with .storylink class
titles = soup.select('.storylink')

# Select all elements with .score class
scores = soup.select('.score')

def scrab_hn():
    titleMod = []
    for i, title in enumerate(titles):
        titleMod.append({
            'title': chalk.blue(title.get_text()),
            'score_sort': int(scores[i - 1].get_text().replace(' points', '')),
            'score': chalk.green('- ' + scores[i - 1].get_text()),
            'link': f"\n{chalk.yellowBright(title.get('href'))}"})
        
    # Loop through a sorted array by score value
    for i, title in enumerate(sorted(titleMod, key=lambda k:k['score_sort'])):
        print(f'\n{i + 1} -', title['title'], title['score'], title['link'], '\n\n')
    return ''

if __name__ == '__main__':
    print(scrab_hn())
