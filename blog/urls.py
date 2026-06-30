#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/06/13 16:38
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: MyBlog
# @FileName   : MyBlog/urls.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from blog import views

urlpatterns = [
    path('/', views.index),
]
