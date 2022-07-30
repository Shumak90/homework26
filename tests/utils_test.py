import pytest
from utils import DataComments

key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


@pytest.fixture()
def data_comments():
    data = DataComments("./data/data.json", "./data/comments.json")
    return data


def test_get_posts_all(data_comments):
    print(set(data_comments.get_posts_all()[0].keys()))
    assert set(data_comments.get_posts_all()[0].keys()) == key_data, "неверный список ключей"
    assert type(data_comments.get_posts_all()) == list, "возвращается не список"