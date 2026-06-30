#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/06/13 16:43
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: MyBlog
# @FileName   : MyBlog/permissions.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    自定义权限：只允许文章的作者编辑/删除它，其他人只能查看。
    """

    def has_object_permission(self, request, view, obj):
        # 任何请求都允许读取权限 (GET, HEAD, OPTIONS)
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # 写入权限 (PUT, PATCH, DELETE) 只允许给文章的作者
        return obj.author == request.user
