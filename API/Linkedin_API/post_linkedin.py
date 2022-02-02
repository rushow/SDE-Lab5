# %%
import json
import io
import traceback

# %%
import requests
from bs4 import BeautifulSoup

def get_hashtagslist(string):
    ret = []
    s=''
    hashtag = False
    for char in string:
        if char=='#':
            hashtag = True
            if s:
                ret.append(s)
                s=''           
            continue

        # take only the prefix of the hastag in case contain one of this chars (like on:  '#happy,but i..' it will takes only 'happy'  )
        if hashtag and char in [' ','.',',','(',')',':','{','}'] and s:
            ret.append(s)
            s=''
            hashtag=False 

        if hashtag:
            s+=char

    if s:
        ret.append(s)

    return ret

from datetime import date, timedelta
def get_date(date_str):
    # days=0
    # seconds=0
    # microseconds=0
    # milliseconds=0
    # minutes=0
    # hours=0
    # weeks=0
    today = date.today()
    date_str = date_str.replace('Edited', '').replace('•', '').replace('·','').replace('\n', '').strip()
    if 'mo' in date_str:
        num = int(date_str.replace('mo', ''))
        return today - timedelta(days=num*365.25/12)
        
    if 'm' in date_str:
        num = int(date_str.replace('m', ''))
        return today - timedelta(minutes=num)
        
    if 'd' in date_str:
        num = int(date_str.replace('d', ''))
        return today - timedelta(days=num)
        
    if 'h' in date_str:
        num = int(date_str.replace('h', ''))
        return today - timedelta(hours=num)
        
    if 'w' in date_str:
        num = int(date_str.replace('w', ''))
        return today - timedelta(weeks=num)

    if 'yr' in date_str:
        num = int(date_str.replace('yr', ''))
        return today - timedelta(days=num*365.25)

    return today

texts = ['3m','5mo', '3d', '23h', '8w', '8yr']

for text in texts:
    print(text + ' -> ' + str(get_date(text)))


# url = "https://www.linkedin.com/posts/tom-alder_strategy-fintech-payments-activity-6835038759793381376-gz2F"
def get_post(url):
    cookies = {'bcookie': 'v=2&28333265-0d6c-4c5a-8268-fb0dc7861f89'}
    response = requests.request("GET", url, cookies=cookies)
    if ('// Parse the tracking code from cookies.' in response.text):
        print('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    like_count = soup.find('span', {'class':'social-counts-reactions__social-counts-numRections'})
    comment_count = soup.find('a', {'data-tracking-control-name':'public_post_share-update_social-details_social-action-counts_comments-text'})
    author_info = soup.find('p', {'class':'share-update-card__actor-headline'})
    content = soup.find('p', {'class':'share-update-card__update-text'})
    author = soup.find('a', {'class':'share-update-card__actor-text-link'})
    date = soup.find('time', {'class':'share-update-card__post-date'})
    related_topics = soup.find_all('a', {'data-tracking-control-name':'public_post_related-topics-pill'})
    approx_date = get_date(date.text.strip())
    row = {
        'type': 'Page Post Linkedin',
        'linkedin_url': url,
        'author': author.text.strip() if author is not None else '',
        'author_info': author_info.text.strip() if author_info is not None else '',
        'date': date.text.strip() if date is not None else '',
        'approx_date': str(approx_date) if date is not None else '',
        'content': content.text.strip() if content is not None else '',
        'related_topics': [i.text.strip() for i in related_topics] if related_topics is not None else [],
        'hashtags': get_hashtagslist(content.text.strip()),
        'like_count': like_count.text.strip() if like_count is not None else '0',
        'comment_count': comment_count.text.strip() if comment_count is not None else '0'
    }
    return row
# %%

def crawl(range_from, range_to):
    links = []
    with open('list_posts_v2.txt', 'r') as f:
        for text in f.readlines():
            links.append(text)


    result_list = []
    last_link = ''
    try:
        print(f'From {range_from} to {range_to}')
        for content in links[range_from:range_to]:
            last_link = content
            dct = get_post(content)
            result_list.append(dct)
            if len(result_list) % 100 == 0:
                print(len(result_list))

        with open(f'list_post_contents_v2_{range_from}_{range_to}.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, indent=4)
    except:
        print(f'Error stoped at {len(result_list)}, {last_link}')
        with open(f'list_post_contents_v2_{range_from}_{range_to}.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, indent=4)

        errors = io.StringIO()
        traceback.print_exc(file=errors)
        contents = str(errors.getvalue())
        print(contents)
        errors.close()

# %%



