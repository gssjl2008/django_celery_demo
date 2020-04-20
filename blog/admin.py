from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link
# Register your models here.


@admin.register(Article)
class Article_admin(admin.ModelAdmin):
    # 文章列表里想要显示的字段
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 满50条数据自动分页
    list_per_page = 10
    # 后台数据列表排序方式
    ordering = ('-created_time',)
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class Banner_admin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class Tui_admin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class Link_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')
