import pytest
from app import app

key_data = ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']


def test_app_all():
    response = app.test_client().get("/api/posts")
    assert type(response.json) == list
    assert list(response.json[0].keys()) == key_data, "неверный список ключей"


def test_app_post():
    response = app.test_client().get("/api/posts/1")
    assert type(response.json) == dict
    assert list(response.json.keys()) == key_data