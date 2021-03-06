#  This is a catcher for https://www.midi.com.au/in-the-style-of/all-artists/*/

import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#
import os
import traceback
from time import time, sleep
from random import random
import pickle


class AuMidCatcher:
    def __init__(self, load=0):
        if os.path.exists('mids') is False:
            os.makedirs('mids')
        self.artist_dict = {}
        self.songs_dict = {}
        self.last_artist = ''
        self.last_song = ''

        if load:
            self.load_labels()

    def download(self, url, filename, enable_debug_info = False):
        if os.path.exists(filename):
            print('file exists!')
            return
        try:
            start_time = time()

            r = requests.get(url, stream=True, timeout=60)
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()

            end_time = time()
            if enable_debug_info:
                print("%s downloaded.  Time: %f s.  Size: %f MB."
                      % (filename,
                         end_time - start_time,
                         os.path.getsize(filename)/1024/1024
                         )
                      )

            return filename
        except KeyboardInterrupt:
            if os.path.exists(filename):
                os.remove(filename)
            raise KeyboardInterrupt
        except Exception:
            traceback.print_exc()
            if os.path.exists(filename):
                os.remove(filename)

    def catch_list(self,s=0, n=331, download=1, debug = 0):
        for i in range(s, n+1):
            url = "https://www.midi.com.au/in-the-style-of/all-artists/" + str(i)
            html = requests.get(url).text
            soup = BeautifulSoup(html,'html5lib')

            for alt in soup.find_all("div", attrs={"class": "top-artist-name left"}):
                url_artist = alt.find('a')["href"]
                #print(url_artist)
                self.catch_artist(url_artist, download, debug)
            if debug:
                print('%d / %d pages finished!' % (i, n))
            self.dump_labels()

    def catch_artist(self, url, download, debug=0):
        status = 0
        while status is not requests.codes.ok:
            sleep(random())
            try:
                r = requests.get(url, timeout=10)
                status = r.status_code
            except Exception:
                traceback.print_exc()

        html = r.text
        soup = BeautifulSoup(html, 'html5lib')

        article = soup.find('article', attrs={"id": "artist"})
        artist = article.find('h1').text.split(' MIDI')[0]
        p1 = article.find('p')
        introduction = p1.text
        p2 = p1.find_next('p')
        genres = p2.text
        related_artists = [a.text for a in article.find_all('a')]

        songs = soup.find('article', attrs={'id': 'songs'})
        songs_list = []
        for span in songs.find_all('span', attrs={'class': 'song-title to-cart'}):

            if 'MIDI' not in span.find_next_sibling('div', attrs={'class': 'feature'}).text:
                continue

            sid = span['id'][2:]  # "s_PPM11128"
            raw_url = span.find('a')['href']
            # https://www.midi.com.au/adele/rolling-in-the-deep-midi/
            # http://www.mididb.com/adele/rolling-in-the-deep-midi/
            url = 'http://www.mididb.com/' + raw_url.split('.au/')[1]
            title = span.find_next('span').text
            songs_list.append((sid, title))
            self.catch_mid(sid, url, title, artist, download, debug)

        dic = {'artist': artist,
               'introduction': introduction,
               'genres': genres,
               'related_artists': related_artists,
               'songs_list': songs_list}

        self.artist_dict[artist] = dic
        if debug:
            print("%s's songs finished!" % artist)

        # log
        self.last_artist = artist
        pickle.dump(self.last_artist, open(os.path.join('mids', 'last_artist.pkl'), 'wb'))


        return dic

    def catch_mid(self, sid, url, title, artist, download=1, debug=0):
        wait = random()
        print('Wait in %f seconds' % wait)
        sleep(wait)

        # get lyric
        lyrics = ''
        lyurl = 'https://www.midi.com.au/' + url.split('.com/')[1]+'lyrics/'
        r = requests.get(lyurl)
        if r.status_code == requests.codes.ok:
            ly_soup = BeautifulSoup(r.text, 'html5lib')
            article = ly_soup.find('article', attrs={'id': 'song'})
            #for br in article.find_all('br'):
            lyrics += article.text
        else:
            print('%s: %s has no lyrics found!' % (sid, title))

        dlurl = 'http://www.mididb.com/midi-download/AUD_%s.mid' % sid
        filename = os.path.join('mids', sid+'.mid')
        if download:
            self.download(dlurl, filename, debug)
        self.songs_dict[sid] = {'title': title,
                                'artist': artist,
                                'lyrics': lyrics}

        # log
        self.last_song = title
        pickle.dump(self.last_song, open(os.path.join('mids', 'last_song.pkl'), 'wb'))

    def dump_labels(self):
        pickle.dump(self.songs_dict, open(os.path.join('mids', 'songs_dict.pkl'), 'wb'))
        pickle.dump(self.artist_dict, open(os.path.join('mids', 'artist_dict.pkl'), 'wb'))

    def load_labels(self):
        self.artist_dict = pickle.load(open(os.path.join('mids', 'artist_dict.pkl'), 'rb'))
        self.songs_dict = pickle.load(open(os.path.join('mids', 'songs_dict.pkl'), 'rb'))
        print('Existing labels loaded！')

    def load_log(self):
        self.last_artist = pickle.load(open(os.path.join('mids', 'last_artist.pkl'), 'rb'))
        self.last_song = pickle.load(open(os.path.join('mids', 'last_song.pkl'), 'rb'))

    def show_log(self):
        print(self.last_artist)
        print(self.last_song)


C = AuMidCatcher(load=1)
C.load_log()

# C.catch_list(s=326, n=331, download=0, debug=1) # Axe Bahia
# 318/319
# C.catch_mid('ST6319', 'https://www.midi.com.au/adele/rolling-in-the-deep-midi', 'Rolling In The Deep', 'Adele', 0, 1)
# print(C.songs_dict)
# print(C.artist_dict)














