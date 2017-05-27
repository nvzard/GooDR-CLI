import click
import requests
from bs4 import BeautifulSoup

@click.command()
@click.option('--pages', default=1, help='No. of pages upto which you need the list of writers[MAX=100]')


def cli(pages):
	"""This script lists all the writes from www.goodreads.com"""
	print("***LIST OF WRITERS***\n\n")
	page = 1
	while page <= pages:
		print("<-----PAGE-",page,"----->\n")
		url = 'https://www.goodreads.com/quotes?page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"html.parser")
		for link in soup.find_all('div',{'class':'quoteText'}):
			for a in link.find_all('a'):
				authors = a.string
				print(authors)
		page += 1
		print("\n")
	print("\n****END****")
	
