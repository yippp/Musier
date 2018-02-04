# README

## 1. Midi文件的爬虫

​	目录 \MidCatcher

### a. \MidCatcher\aumidcatcher.py

​	面向对象封装的爬虫，基于

```python
requests
bs4
```

​	**仅针对```https://www.midi.com.au/```上的内容**

​	目前进度：

​		.mid 文件 和 labels 都爬完了，但是对应关系和数据清洗还没做

### b. \MidCathcer\mids\

#### 	i. *.mid

​		midi音频文件，文件名是其对应的 sid

#### 	ii. artist_dict.pkl

​		艺术家相关信息，pkl 里是一个 dictionary

```python
artist_dict[<artist_name>] = {'artist': artist,  # str, same as <artist_name>
          					  'introduction': introduction,  # str
         				      'genres': genres,  # str
         				      'related_artists': related_artists,  # list of str
        				      'songs_list': songs_list  # list of str
        				      }
```
#### 	iii. songs_dict.pkl

​		每首歌的信息，pkl 里是一个 dictionary

```python
songs_dict[<sid>] = {'title': title,  # note <sid> is a str
                     'artist': artist,
                     'lyrics': lyrics
                    }
```

#### 	iv.  last_song.pkl & last_artist.pkl

​			爬虫爬过的最后的歌和艺术家的名字，仅供 log 用

​			