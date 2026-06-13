from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 现在什么都不用加，继承原有的 username, password, email 等就够了
    pass


class Category(models.Model):
    """分类表，只保留最核心的分类"""
    name = models.CharField('分类', max_length=50, unique=True)

    class Meta:
        db_table = 'blog_category'
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="正文")
    # 外键关联分类，一对多。一个分类下有多篇文章
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="分类")
    # 外键关联用户，一对多。一个用户可以发多篇文章
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'blog_article'
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """评论表，支持自关联"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评论者")
    content = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="父评论",
        related_name='replies'
    )

    class Meta:
        db_table = 'blog_comment'
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username}: {self.content[:8]}..."
