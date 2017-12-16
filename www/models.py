#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time
import uuid

from orm import Model, StringField, BooleanField, FloatField, TextField
import asyncio
import orm
import sys


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

# async def test(loop):
#     await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
#     # u = User(name='test', email='test@test.com',
#     #          passwd='11111', image='about:blank')
#     # await u.save()
#     blog = Blog(user_id='', user_name='test', user_image='about:blank',
#                 name='test', summary='tested', content='halo,world')
#     await blog.save()
#     # await orm.destroy_pool()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()
# # if loop.is_closed():
# #     sys.exit(0)
