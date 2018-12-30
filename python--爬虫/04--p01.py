'''
爬取豆瓣电影剧情排行榜
了解Ajax的基本爬取方式
'''
from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

rsp = request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)
print(data)
'''
{'rating': ['9.2', '50'],
 'rank': 41, 
 'cover_url': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2029574250.jpg',
 'is_playable': False, 
 'id': '4719384', 
 'types': ['剧情', '爱情', '家庭'], 
 'regions': ['中国大陆'], 
 'title': '哀乐中年',
 'url': 'https://movie.douban.com/subject/4719384/', 
 'release_date': '1949',
 'actor_count': 19, 
 'vote_count': 6023,
 'score': '9.2',
 'actors': ['石挥', '朱嘉琛', '沈扬', '李浣青', '韩非', '崔超明', '程之', '路珊', '莫愁', '胡小琴', '顾慕如', '俞仲英', '伊斯兰', '叶明', '林榛', '田振东', '周瑞德', '姚思诚', '于复瑛'],
 'is_watched': False}, 
 ...
'''