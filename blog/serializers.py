#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/06/13 16:43
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: MyBlog
# @FileName   : MyBlog/serializers.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from rest_framework import serializers
from .models import Article, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# 用于文章列表展示的 Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # 自动带出作者名字

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'created_time']


# 用于文章详情和创建的 Serializer
class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = '__all__'
        # 因为前端创建文章时不应该传author，author应该从登录信息里取，所以设为只读
        read_only_fields = ['author']
