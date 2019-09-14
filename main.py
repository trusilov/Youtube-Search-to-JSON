# -*- coding: utf-8 -*-
"""
Simple utility to search for videos
on YouTube and write data in json file.
"""
import json

from datetime import datetime
from static import api_key, key_word, count
from googleapiclient.discovery import build


result = []

#   youtube api
youtube = build('youtube', 'v3', developerKey=api_key)

time = datetime(year=2019, month=8, day=4).strftime("%Y-%m-%dT%H:%M:%SZ")
data = youtube.search().list(q=key_word,
                             part='snippet',
                             type='video',
                             maxResults=count,
                             publishedAfter=time).execute()


for item in sorted(data["items"], key=lambda x: x['snippet']['publishedAt']):
    json_results = {'name': item['snippet']['title'],
                    'pub_date': item['snippet']['publishedAt'],
                    'url': 'https://www.youtube.com/watch?v=' + item['id']['videoId']}
    result.append(json_results)


def main():
    with open('list.json', 'w', ) as file:
        json.dump(result, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
