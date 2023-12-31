import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')

def sort_news(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'],reverse=True)


def custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title':title, 'votes':points})
	return sort_news(hn)


pprint.pprint(custom_hn(links, subtext))