#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import logging
import requests
from requests.exceptions import HTTPError

__version__ = "0.0.1.2"


class Client(object):
    """Client class"""

    _base_url = "https://9gag.com/v1/group-posts/group/"
    _default_group = "default/"
    _fresh_type = "type/fresh"
    _hot_type = "type/hot"
    _trending_type = "type/trending"

    # @classmethod
    # def __init__(cls):
    #     cls.next_cursor = {}

    @classmethod
    def get_posts_by_group(cls, group="default", type="fresh"):
        """Return posts by group"""
        group = re.sub(r'([^A-Za-z])', '', group).lower()
        type = re.sub(r'([^A-Za-z])', '', type).lower()

        url_sufix = group + "/type/" + type
        result = cls._get_api_data(url_sufix)
        return result

    @classmethod
    def get_last_post(cls):
        """Return last post"""
        result = cls.get_fresh_posts()
        return result[0]

    @classmethod
    def get_fresh_posts(cls):
        """Return fresh posts"""
        url_sufix = cls._default_group + cls._fresh_type
        result = cls._get_api_data(url_sufix)
        return result

    @classmethod
    def get_hot_posts(cls):
        """Return hot posts"""
        url_sufix = cls._default_group + cls._hot_type
        result = cls._get_api_data(url_sufix)
        return result

    @classmethod
    def get_trending_posts(cls):
        """Return trending posts"""
        url_sufix = cls._default_group + cls._trending_type
        result = cls._get_api_data(url_sufix)
        return result

    @classmethod
    def _get_api_data(cls, url_sufix):
        """Return json from api"""
        url = cls._base_url + url_sufix
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_response = response.json()
            return cls._format_response(json_response, url_sufix)
        except HTTPError as http_err:
            logging.error('HTTP error occurred: %s', http_err)
        except Exception as err:
            logging.error('Other error occurred: %s', err)
        return False

    @classmethod
    def _format_response(cls, response, url_sufix):
        """Format Response Json"""
        if 'data' in response:
            data = response['data']
            #cls.next_cursor[url_sufix] = data["nextCursor"]
            return data['posts']
        return False
