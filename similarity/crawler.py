import requests
from bs4 import BeautifulSoup

# 目标网站的URL
url = 'https://www.yicai.com/'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到最热栏目的标签和类名（需要实际检查网页结构）
    hot_section = soup.find('div', class_='hot-section-class-name')

    # 在最热栏目中查找所有文章的标题
    titles = hot_section.find_all('h2', class_='title-class-name')

    # 打印所有标题
    for title in titles:
        print(title.text.strip())

    # 对于每个标题，也可以继续查找内容部分
    # ...
else:
    print('Failed to retrieve the webpage')
