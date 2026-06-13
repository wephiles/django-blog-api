# django-blog-api

![LICENSE: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

本项目采用MIT许可证授权——详情请参见`LICENSE`文件。

## 简介

这是一个基于 Django + DRF 的个人博客后端 API。

## 技术栈

Python 3.x / Django 4.x / DRF / MySQL / Redis / Docker / JWT。

## 数据模型&表结构设计

- 用户表 （`User`）
  用户表继承 `Django` 内部的 `AbstractUser`，后面如果有需要可以再增加头像等.

  | id   | username | password | email |
  | ---- | -------- | -------- | ----- |
  |      |          |          |       |
  |      |          |          |       |
  |      |          |          |       |

- 分类表（`Category`）

  | id   | name |
  | ---- | ---- |
  |      |      |

- 文章表（`Article`）

  | id   | title | content | category | author | created_time | updated_time |
  | ---- | ----- | ------- | -------- | ------ | ------------ | ------------ |
  |      |       |         |          |        |              |              |

- 评论表（`Comment`） 支持自关联

  | id   | article | user | content | created_time | parent |
  | ---- | ------- | ---- | ------- | ------------ | ------ |
  |      |         |      |         |              |        |

## 本地运行步骤

...

## 接口示例

...









