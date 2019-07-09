#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ninegagposts


class UnitTests(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(ninegagposts)

    def test_class_instance(self):
        client = ninegagposts.Client()
        self.assertIsInstance(client, ninegagposts.Client)

    def test_last_post(self):
        client = ninegagposts.Client()
        last_post = client.get_last_post()
        self.assertNotEqual(last_post, False)

    def test_fresh_posts(self):
        client = ninegagposts.Client()
        posts = client.get_fresh_posts()
        self.assertNotEqual(posts, False)

    def test_hot_posts(self):
        client = ninegagposts.Client()
        posts = client.get_hot_posts()
        self.assertNotEqual(posts, False)

    def test_trending_posts(self):
        client = ninegagposts.Client()
        posts = client.get_trending_posts()
        self.assertNotEqual(posts, False)

    def test_posts_by_group(self):
        client = ninegagposts.Client()
        posts = client.get_posts_by_group("brazil", "hot")
        self.assertNotEqual(posts, False)
