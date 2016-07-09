#! /usr/bin/env python

import os
import socket
import libtorrent as lt
import time
import urllib2
from urllib2 import HTTPError, URLError, urlopen

#consider miniupnp for networking

BUFF = 1024
host = "127.0.0.1"
port = 9999
torrentName = "recv.torrent"

#this url is for testing
testUrl = "http://127.0.0.1:9999/test.torrent"

def download_torrent_file(url):
    try:
        file = urlopen(url)
        print "downloading " + url
        with open("recv.torrent", "wb") as local_file:
            local_file.write(file.read())

    #error handling
    except HTTPError, e:
        print "HTTP error:", e.code, url
    except URLError, e:
        print "URL error:", e.reason, url

def receive_content():
    ses = lt.session()
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open(torrentName, 'rb').read())
    info = lt.torrent_info(e)

    params = { 'save_path': '.', \
        'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
        'ti': info }
    h = ses.add_torrent(params)

    stats = h.status()
    while (not stats.is_seeding):
        stats = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']

        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
                (stats.progress * 100, stats.download_rate / 1000, stats.upload_rate / 1000, \
                stats.num_peers, state_str[stats.state])

        time.sleep(1)

if __name__ == "__main__":
    download_torrent_file(testUrl)
    receive_content()
    sock.close()
    print('connection closed')
