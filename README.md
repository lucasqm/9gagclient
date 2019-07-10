# Ninegagposts

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
