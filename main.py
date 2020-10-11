import requests
from nested_lookup import nested_lookup

limit = 50  # get max number of items per page
movie_quality = '2160p'  # prefer 4k files
movie_type = 'bluray'  # prefer bluray to web alternatives

req = requests.get(url='https://yts.mx/api/v2/list_movies.json?quality=' + movie_quality)
to_count = req.json()
movie_count = nested_lookup('movie_count', to_count)
total_movies = movie_count[0]
pages = int((total_movies / limit) + 1)
torrents = []
for i in range(1, pages + 1):
    print('Retrieving page: ' + str(i))
    r = requests.get(
        url='https://yts.mx/api/v2/list_movies.json?quality=' + movie_quality + '&limit=' + str(limit) + '&page=' + (
            str(i)))
    data = r.json()
    torrents_temp = nested_lookup('torrents', data)
    torrents.extend(torrents_temp)
my_list = []
for sublist in torrents:
    for item in sublist:
        my_list.append(item)
my_list = list(filter(lambda j: j['quality'] == movie_quality, my_list))
my_list = list(filter(lambda j: j['type'] == movie_type, my_list))
urls = []
file1 = open('yts.txt', 'w')  # save to yts.txt in project folder
for k in my_list:
    key, val = next(iter(k.items()))
    file1.write(str(val) + '\n')
file1.close()
