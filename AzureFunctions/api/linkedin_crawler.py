import requests
from bs4 import BeautifulSoup
import logging
import re

# get_pulse('https://www.linkedin.com/pulse/future-ge-larry-culp')
# {'author': 'Larry Culp',
#  'author_info': 'Chairman & CEO at GE',
#  'comment_count': '210 Comments',
#  'content': 'Even at a company with as storied a history as ours, today is a defining moment for GE. Our announcement to form three industry-leading, global public companies focused on the growth sectors of aviation, healthcare, and energy is the next step in a historic transformation. For nearly 130 years, people have counted on GE to “find out what the world needs and proceed to invent it,” as our founder Thomas Edison so famously said. We carry that forward today not as one organization but as three future companies, all built from that DNA of innovation.We intend to start by standing up GE Healthcare as an independent company at the center of precision health in early 2023. We also plan to combine GE Renewable Energy, GE Power, and GE Digital into one business, positioned to lead the energy transition, and then pursue a spin-off of this business in early 2024. Following these transactions, GE will be an aviation-focused company shaping the future of flight.The world demands – and deserves – we bring our best to solve the biggest challenges in flight, healthcare, and energy. By putting our technology expertise, leadership, and global reach to work to better serve our customers, we will do just that. Each new company will benefit from greater focus, tailored capital allocation, and strategic flexibility to drive long-term growth and value. We are now able to plan for this remarkable next step thanks to your exceptional work strengthening our financial position and operating performance, all while deepening our culture of continuous improvement and lean. \xa0Personally, I remain fully committed to our future. I will serve as non-executive chairman of the GE healthcare company upon the planned spin-off. I will continue to serve as chairman and CEO of GE until the planned second spin-off, at which point, I will lead the GE aviation-focused company going forward. To the GE team – past and present – thank you for your hard work. You have created this opportunity in front of us and I am confident you will make it successful. I couldn’t be prouder to be on this team. LarryFor important information about forward-looking statements involving these transactions, please see here.',
#  'content_title': 'The Future of GE',
#  'date': 'Published Nov 9, 2021',
#  'like_count': '5,784',
#  'linkedin_url': 'https://www.linkedin.com/pulse/future-ge-larry-culp',
#  'type': 'Page Pulse Linkedin'}

def get_pulse(url):
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        print('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    like_count = soup.find('span', {'class':'social-counts-reactions__social-counts-numRections'})
    comment_count = soup.find('a', {'data-tracking-control-name':'pulse-article_social-details_social-action-counts_comments-text'})
    row = {
        'type': 'Page Pulse Linkedin',
        'linkedin_url': url,
        'author': soup.find('h3', {'class':'base-main-card__title'}).text.strip(),
        'author_info': soup.find('h4', {'class':'base-main-card__subtitle'}).text.strip(),
        'date': soup.find('div', {'class':'base-main-card__metadata'}).text.strip(),
        'content_title': soup.find('meta', {'property':'og:title'})['content'],
        'content': soup.find('div', {'class':'article-content__body'}).text.strip(),
        'like_count': like_count.text.strip() if like_count is not None else '0',
        'comment_count': comment_count.text.strip() if comment_count is not None else '0'
    }

    return row


# get_post('https://www.linkedin.com/posts/tom-alder_strategy-fintech-payments-activity-6835038759793381376-gz2F')
# get_post('https://www.linkedin.com/posts/sushil627_reactjs-management-java-activity-6856798337744613376-DmG_?trk=content-search-results-full-link')
# get_post('https://www.linkedin.com/posts/ericmahecha_team-lead-account-management-activity-6880552718872649728-nEKs?trk=content-search-results-full-link')
# {'author': 'Eric Mahecha',
#  'author_info': 'VP, Account Management, North America at Adyen',
#  'comment_count': '0',
#  'content': 'Join Adyen, one of Forbes Future 50 and most innovative Fintech company.\nAdyen is looking for a(n) Team Lead, Account Management to join the team in San Francisco !\nLet us know if you are interested via https://lnkd.in/dKqyYYa7.',
#  'date': '2h',
#  'like_count': '3',
#  'linkedin_url': 'https://www.linkedin.com/posts/ericmahecha_team-lead-account-management-activity-6880552718872649728-nEKs?trk=content-search-results-full-link',
#  'type': 'Page Post Linkedin'}
def get_post(url):
    response = requests.request("GET", url)
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
    row = {
        'type': 'Page Post Linkedin',
        'linkedin_url': url,
        'author': author.text.strip() if author is not None else '',
        'author_info': author_info.text.strip() if author_info is not None else '',
        'date': date.text.strip() if date is not None else '',
        'content': content.text.strip() if content is not None else '',
        'like_count': like_count.text.strip() if like_count is not None else '0',
        'comment_count': comment_count.text.strip() if comment_count is not None else '0'
    }
    return row

# url = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/2846001789"
# get_job(2846000000)
# get_job(2843000055)
# {'company_url': None,
#  'description': '该职位来源于猎聘岗位描述：配合项目工程师评估尺寸精密测量及无损分析相关（CT、超声扫描显微镜等）的业务咨询；执行精密测量及无损分析的业务，按节点输出相关业务报告；负责相关设备的操作、维护及培训（工业三坐标、CT、超声扫描显微镜等），包括操作指导书更新、设备使用及维修记录等；配合领导完成实验室相关能力建设工作，如设备调研等；实验室5s维护及其他领导安排的工作。职位要求：本科及以上学历，机械、微电子等相关专业；2.3年以上精密测量/电子领域相关工作经验；可熟练操作三坐标/光学投影仪，同时具备超声扫描显微镜、CT等无损分析设备经验的优先；有蔡司三坐标、CT培训证书的优先；逻辑清晰，理解能力强，有实验室工作经验的优先。\n\n\n        Show more\n\n        \n\n\n        Show less',
#  'linkedin_url': 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/2843000055',
#  'location': 'Shanghai, Shanghai, China',
#  'meta': {'Employment type': 'Full-time',
#   'Industries': 'Automation Machinery Manufacturing',
#   'Job function': 'Engineering and Information Technology',
#   'Seniority level': 'Entry level'},
#  'title': '失效分析工程师（无损）',
#  'type': 'Job Description Linkedin'}

def get_job(job_id):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"

    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        logging.error('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    link_to_company = soup.find('a', {'class':'apply-button apply-button--link top-card-layout__cta top-card-layout__cta--primary'})
    row = {
        'type': 'Job Description Linkedin',
        'company_url': link_to_company['href'] if link_to_company is not None else None,
        'linkedin_url': f'https://www.linkedin.com/jobs/view/{job_id}',
        'title': soup.find('h2', {'class':'top-card-layout__title topcard__title'}).text,
        'location': soup.find('span', {'class':'topcard__flavor topcard__flavor--bullet'}).text.strip(),
        'description': soup.find('div', {'class':'description__text description__text--rich'}).text.strip(),
        'meta': dict([(e.find('h3').text.strip(), e.find('span').text.strip()) for e in soup.find_all('li', {'class':'description__job-criteria-item'})]),
    }
    return row

# Get topics from https://www.linkedin.com/content-hub
def get_main_hub_topics():
    url = "https://www.linkedin.com/content-hub"
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        logging.error('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    return dict([(e.text.strip(), e['href']) for e in soup.find_all('a', {'data-tracking-control-name':'content-hub-home_explore-career-topics-pill'})])

# Get child topics from 'https://www.linkedin.com/content-hub/accounting-f1/?trk=content-hub-home_explore-career-topics-pill'
# Can recursive child in child
# get_child_hub_topics('https://www.linkedin.com/content-hub/accounting-f1/?trk=content-hub-home_explore-career-topics-pill')
def get_child_hub_topics(url):
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        logging.error('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    return dict([(e.text.strip(), e['href']) for e in soup.find_all('a', {'data-tracking-control-name':'aside-explore-pill'})])


# get_post_links_in_topic('https://www.linkedin.com/content-hub/marketing-and-advertising-692298/?trk=homepage-basic_explore-content_topic-pill')
def get_post_links_in_topic(url):
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text):
        logging.error('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    return [(e['href']) for e in soup.find_all('a', {'data-tracking-control-name':'content-search-results-full-link'})]

# Large requests
def get_hub_topics():
    main = get_main_hub_topics()
    lstDict = []
    for key, val in main.items():
        lstDict.append(get_child_hub_topics(val))

    for item in lstDict:
        main.update(item)

    return main

# Large requests. I have crawled 77K post links in Linkedin_API folder, but only get these 5K posts content (30min)
def get_post_links_in_hub_content():
    topics = get_hub_topics()
    print(len(topics))
    posts = []
    for key, val in topics.items():
        posts.extend(get_post_links_in_topic(val))

    return posts

# use for search the specific location, ex Trento -> return geoId to use in search_job for more accurately
def search_geo_id(geo_text):
    url = f'https://www.linkedin.com/jobs-guest/api/typeaheadHits?query={geo_text}&typeaheadType=GEO&geoTypes=POPULATED_PLACE,ADMIN_DIVISION_2,MARKET_AREA,COUNTRY_REGION'
    response = requests.request("GET", url)
    return response.text

# search_job('Computer Science', 'Colorado', paging = 1)
def search_job(job_title, location, paging, geo_id = ''):
    start = 25*int(paging)
    url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?location={location}&geoId={geo_id}&keywords={job_title}&start={start}'
    response = requests.request("GET", url)
    if ('// Parse the tracking code from cookies.' in response.text or 'Join to use advanced searches for free' in response.text):
        logging.error('Cannot bypass the cookies')
        return None

    soup = BeautifulSoup(response.text.replace('data-tracking-client-ingraph','').replace('data-tracking-will-navigate', ''), 'html.parser')
    lst = []
    elements = soup.find_all('div', {'class': 'base-search-card__info'})
    if (len(elements) == 0):
        logging.error(f'Error with {url}')
        return []

    for item in elements:
        parent = item.parent.find('a',{'data-tracking-control-name':'public_jobs_jserp-result_search-card'})
        row = {
            'type': f'Linkedin Query: Job Title {job_title}, at {location}, geo id {geo_id}, page {paging}',
            'id': re.search("[-](\d+)[?refId]", parent['href']).group(1) if parent is not None else '',
            'linkedin_url': parent['href'] if parent is not None else '',
            'title': item.find('h3', {'class':'base-search-card__title'}).text.strip(),
            'subtitle': item.find('h4', {'class':'base-search-card__subtitle'}).text.strip(),
            'meta': item.find('div', {'class':'base-search-card__metadata'}).text.strip(),
        }
        lst.append(row)

    return lst

