import json


class DataComments:
    def __init__(self, path_data, path_comments, path_book):
        self.path_data = path_data
        self.path_comments = path_comments
        self.path_book = path_book

    def get_posts_all(self):
        """возвращает посты"""
        with open(self.path_data, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя"""
        data_all = self.get_posts_all()
        data_user_all = []
        for data_user in data_all:
            if user_name == data_user["poster_name"]:
                data_user_all.append(data_user)
        return data_user_all

    def get_comments_by_post_id(self, post_id):
        """возвращает комментарии определенного поста"""
        with open(self.path_comments, "r", encoding="utf-8") as file:
            comments_all = json.load(file)
        comments = []
        for comment in comments_all:
            if post_id == comment["post_id"]:
                comments.append(comment)
        return comments

    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        data_all = self.get_posts_all()
        query_posts = []
        for data in data_all:
            if query.lower() in data["content"].lower():
                query_posts.append(data)
        return query_posts

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору"""
        data_all = self.get_posts_all()
        for data in data_all:
            if pk == data["pk"]:
                return data

    def get_add_bookmarks_post_id(self, post_id):
        """добавление в закладки"""
        with open(self.path_book, "r", encoding="utf-8") as file:
            data = json.load(file)
        data.append(self.get_post_by_pk(post_id))
        x = []
        for i in data:
            if i not in x:
                x.append(i)
        data = x
        with open(self.path_book, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def del_bookmarks(self, post_id):
        """удаление закладок"""
        with open(self.path_book, "r", encoding="utf-8") as file:
            data = json.load(file)
        x = []
        for i in data:
            if i not in [self.get_post_by_pk(post_id)]:
                x.append(i)
        data = x
        with open(self.path_book, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def all_bookmarks(self):
        """возвращает закладки"""
        with open(self.path_book, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def len_bookmarks(self):
        data = self.all_bookmarks()
        return len(data)

    def add_comments(self, post_id, name, comment):
        """добавить комментарий"""
        with open(self.path_comments, "r", encoding="utf-8") as file:
            comments_all = json.load(file)
        pk = len(comments_all)
        comments = {"post_id": post_id, "commenter_name": name, "comment": comment, "pk": pk+1}
        for comment in comments_all:
            if pk == comment["pk"]:
                comments_all.append(comments)
        with open(self.path_comments, "w", encoding="utf-8") as file:
            json.dump(comments_all, file, indent=2, ensure_ascii=False)


# p = DataComments("data/data.json", "data/comments.json", "data/bookmarks.json")
