from django.urls import path
from .views import (
    home,
    login_view,
    register_view,
    add_blog,
    see_blog,
    blog_detail,
    blog_update,
    blog_delete,
    logout_view,
)

# from .views import

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path("add_blog/", add_blog, name="add_blog"),
    path("see_blog/", see_blog, name="see_blog"),
    path("blog_details/<slug>", blog_detail, name="blog_detail"),
    path("see_blog", see_blog, name="see_blog"),
    path("blog-delete/<id>", blog_delete, name="blog_delete"),
    path("blog-update/<slug>/", blog_update, name="blog_update"),
    path("logout_view/", logout_view, name="logout_view"),
]
