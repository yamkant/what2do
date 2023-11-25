import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/topic/stock-market-news/'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # 예제: 모든 기사 제목과 링크 출력
    articles = soup.find_all('h3', class_='Mb(5px)')
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href']
        print(f'Title: {title}\nLink: {link}\n')

else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')