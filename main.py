import requests
from nested_lookup import nested_lookup
import os

# Define requirements

limit = 50  # get max number of items per page
movie_quality = '2160p'  # prefer 4k files
movie_type = 'bluray'  # prefer bluray to web alternatives
save_path = 'D:/HGST/qBittorrent/Torrents'  # where to save *.torrent

# Get total number of movies to download

req = requests.get(url='https://yts.mx/api/v2/list_movies.json?quality=' + movie_quality)
to_count = req.json()
movie_count = nested_lookup('movie_count', to_count)
total_movies = movie_count[0]
pages = int((total_movies / limit) + 1)
torrents = []

# Parse JSON to list

for i in range(1, pages + 1):
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

my_urls = []
for k in my_list:
    key, val = next(iter(k.items()))
    my_urls.append(val)

# Download list of URLs to *.torrent file

for urls in my_urls:
    i_req = requests.get(urls, allow_redirects=True)
    file_name = i_req.url.split("/")[-1] + '.torrent'
    my_file = open(os.path.join(save_path, file_name), 'wb')
    my_file.write(i_req.content)
    my_file.close()

# TODO: Better file naming system, rather than relying on Hash of torrent file.
# TODO: Enhance performance if possible (file I/O may cause performance degradation?
# TODO: Show better progress meters
# TODO: Implement Command line scripting
# TODO: Optimize imports?
