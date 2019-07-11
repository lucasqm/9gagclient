Ninegagposts
============================

![PyPI](https://img.shields.io/pypi/v/ninegagposts.svg)
[![GitHub license](https://img.shields.io/github/license/lucasqm/9gagclient.svg)](https://github.com/lucasqm/9gagclient/blob/master/LICENSE)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ninegagposts.svg)

------------------------------------------------------------------------

This is a python client to get [9Gag](https://9gag.com) posts

### Installation

Ninegagposts requires [Python](https://www.python.org/) 3.6+ to run.

```sh
$ pip install ninegagposts
```

### Examples

Get Last Post:
```python
from ninegagposts import Client

Client.get_last_post() #returns a dictionary
```

Output Example:
```json
{
  "id": "aB07d02",
  "url": "http://9gag.com/gag/aB07d02",
  "title": "I gotta get one of those",
  "type": "Animated",
  "nsfw": 0,
  "upVoteCount": 0,
  "downVoteCount": 0,
  "creationTs": 1562853914,
  "promoted": 0,
  "isVoteMasked": 1,
  "hasLongPostCover": 0,
  "images": {
    "image700": {
      "width": 460,
      "height": 571,
      "url": "https://img-9gag-fun.9cache.com/photo/aB07d02_460s.jpg"
    },
    "image460": {
      "width": 460,
      "height": 571,
      "url": "https://img-9gag-fun.9cache.com/photo/aB07d02_460s.jpg",
      "webpUrl": "https://img-9gag-fun.9cache.com/photo/aB07d02_460swp.webp"
    },
    "image460sv": {
      "width": 460,
      "height": 570,
      "url": "https://img-9gag-fun.9cache.com/photo/aB07d02_460sv.mp4",
      "hasAudio": 1,
      "duration": 44
    },
    "image460svwm": {
      "width": 460,
      "height": 570,
      "url": "https://img-9gag-fun.9cache.com/photo/aB07d02_460svwm.webm",
      "hasAudio": 1,
      "duration": 44
    }
  },
  "sourceDomain": "",
  "sourceUrl": "",
  "commentsCount": 0,
  "postSection": {
    "name": "Video",
    "url": "https://9gag.com/video",
    "imageUrl": "https://miscmedia-9gag-fun.9cache.com/images/thumbnail-facebook/1557283964.0386_avUmy5_100x100.jpg"
  },
  "tags": [],
  "descriptionHtml": ""
}
```

----------------------------------------------

Get Fresh Posts:
```python
from ninegagposts import Client

Client.get_fresh_posts() #returns a dictionary list
```

Get Hot Posts:
```python
from ninegagposts import Client

Client.get_hot_posts() #returns a dictionary list
```

Get Trending Posts:
```python
from ninegagposts import Client

Client.get_trending_posts() #returns a dictionary list
```

Get Posts by Group:
```python
from ninegagposts import Client

Client.get_posts_by_group(group="default", type="fresh") #returns a dictionary list
```

Output Example:

```json
[
  {
    "id": "awA6Zor",
    "url": "http://9gag.com/gag/awA6Zor",
    "title": "Kinetic Energy - Homage to Alfonso Wong",
    "type": "Photo",
    "nsfw": 0,
    "upVoteCount": 0,
    "downVoteCount": 0,
    "creationTs": 1562854100,
    "promoted": 0,
    "isVoteMasked": 1,
    "hasLongPostCover": 0,
    "images": {
      "image700": {
        "width": 700,
        "height": 1084,
        "url": "https://img-9gag-fun.9cache.com/photo/awA6Zor_700b.jpg",
        "webpUrl": "https://img-9gag-fun.9cache.com/photo/awA6Zor_700bwp.webp"
      },
      "image460": {
        "width": 460,
        "height": 712,
        "url": "https://img-9gag-fun.9cache.com/photo/awA6Zor_460s.jpg",
        "webpUrl": "https://img-9gag-fun.9cache.com/photo/awA6Zor_460swp.webp"
      }
    },
    "sourceDomain": "",
    "sourceUrl": "",
    "commentsCount": 0,
    "postSection": {
      "name": "Countryballs",
      "url": "https://9gag.com/countryballs",
      "imageUrl": "https://miscmedia-9gag-fun.9cache.com/images/thumbnail-facebook/1557310697.557_Ba4aSa_100x100.jpg"
    },
    "tags": [],
    "descriptionHtml": ""
  },
  {
    "id": "a5M8XRN",
    "url": "http://9gag.com/gag/a5M8XRN",
    "title": "Americat",
    "type": "Photo",
    "nsfw": 0,
    "upVoteCount": 0,
    "downVoteCount": 0,
    "creationTs": 1562854100,
    "promoted": 0,
    "isVoteMasked": 1,
    "hasLongPostCover": 0,
    "images": {
      "image700": {
        "width": 700,
        "height": 52,
        "url": "https://img-9gag-fun.9cache.com/photo/a5M8XRN_700b.jpg",
        "webpUrl": "https://img-9gag-fun.9cache.com/photo/a5M8XRN_700bwp.webp"
      },
      "image460": {
        "width": 460,
        "height": 34,
        "url": "https://img-9gag-fun.9cache.com/photo/a5M8XRN_460s.jpg",
        "webpUrl": "https://img-9gag-fun.9cache.com/photo/a5M8XRN_460swp.webp"
      }
    },
    "sourceDomain": "",
    "sourceUrl": "",
    "commentsCount": 0,
    "postSection": {
      "name": "Countryballs",
      "url": "https://9gag.com/countryballs",
      "imageUrl": "https://miscmedia-9gag-fun.9cache.com/images/thumbnail-facebook/1557310697.557_Ba4aSa_100x100.jpg"
    },
    "tags": [],
    "descriptionHtml": ""
  }
]
```
