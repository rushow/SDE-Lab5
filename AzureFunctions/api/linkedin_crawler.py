import requests
from bs4 import BeautifulSoup

# url = "https://www.linkedin.com/pulse/future-ge-larry-culp"
# get_page('https://www.linkedin.com/pulse/future-ge-larry-culp')

def get_page(url):
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        print('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    row = {
        'author': soup.find('h3', {'class':'base-main-card__title'}).text.strip(),
        'author_info': soup.find('h4', {'class':'base-main-card__subtitle'}).text.strip(),
        'date': soup.find('div', {'class':'base-main-card__metadata'}).text.strip(),
        'content_title': soup.find('meta', {'property':'og:title'})['content'],
        'content': soup.find('div', {'class':'article-content__body'}).text.strip(),
        'like_count': soup.find('span', {'class':'social-counts-reactions__social-counts-numRections'}).text.strip(),
        'comment_count': soup.find('a', {'data-tracking-control-name':'pulse-article_social-details_social-action-counts_comments-text'}).text.strip()
    }

    return row
