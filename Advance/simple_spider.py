import requests
from bs4 import BeautifulSoup

"""
两个简单的爬虫栗子，爬取豆瓣电影TOP250与爬取廖雪峰Python教程每一篇的阅读量
第一个例子在完成每页的数据抽取之后，递归爬取下一页的内容
第二个例子因为每个页面的下一页按钮的链接是伪元素::before，不清楚如何获取，所以直接爬取了树状列表的URL之后再统一爬取每页数据
"""

test_url = 'http://movie.douban.com/top250/'
base_url = 'https://www.liaoxuefeng.com'
target_url = 'https://www.liaoxuefeng.com/wiki/1016959663602400'
movie_name_list = []
numbers = []
url_list = []


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    if movie_list_soup is not None:
        for movie_li in movie_list_soup.find_all('li'):
            detail = movie_li.find('div', attrs={'class': 'hd'})
            movie_name = detail.find('span', attrs={'class': 'title'}).getText()
            movie_name_list.append(movie_name)
        next_page = soup.find('span', attrs={'class': 'next'}).find('a')
        if next_page:
            parse_html(download_page(test_url + next_page['href']))
        return movie_name_list


def get_url(html):
    soup = BeautifulSoup(html, features='html.parser')
    target = soup.find('ul', attrs={'id': 'x-wiki-index'})
    if target is not None:
        for link in target.find_all('a'):
            url_list.append(str(link['href']))
    return url_list


def parse_number(html):
    soup = BeautifulSoup(html, features='html.parser')
    target = soup.find('div', attrs={'class': 'x-wiki-info'})
    if target is not None:
        number_str = str(target.find('span').getText())
        numbers.append(number_str[7:])
        next_page = soup.find('div', attrs={'class': 'x-wiki-prev-next'})
        return numbers


def douban_movie():
    handle = parse_html(download_page(test_url))
    if handle is not None:
        handle = list(handle)
        for ele in handle:
            print(ele)


def student_num():
    get_url(download_page(target_url))
    for url in url_list:
        parse_number(download_page(base_url+url))
    print(list(numbers))


if __name__ == '__main__':
    # 爬取豆瓣电影TOP250标题
    douban_movie()
    # 爬取python教程每页的阅读量
    # student_num()
