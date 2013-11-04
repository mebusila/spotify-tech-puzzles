#!/usr/bin/env python

__author__ = 'Serban Carlogea'
__email__ = 'sherban.carlogea@gmail.com'

import sys


def get_songs(songs, how_many):
    __songs = []
    for song in songs:
        __info = song.split()
        __songs.append({'t': __info[0], 'n': __info[1]})
    for i in range(0, len(__songs)):
        __songs[i]['q'] = int(__songs[i]['t']) * (i+1)
    return sorted(__songs, key=lambda s: s['q'], reverse=True)[:how_many]

if __name__ == '__main__':
    content = []
    for line in sys.stdin:
        content.append(line.strip('\n'))

    info = map(int, content[0].split())
    print '\n'.join([item['n'] for item in get_songs(content[1:info[0] + 1], info[1])])
