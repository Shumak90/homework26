from flask import Flask, request, render_template, jsonify, redirect
from utils import DataComments

app = Flask(__name__)

data = DataComments("./data/data.json", "./data/comments.json", "./data/bookmarks.json")


@app.route("/")
def index():
    return render_template("index.html", all_post=data.get_posts_all(), len_bookmark=data.len_bookmarks())


@app.route("/posts/<int:postid>", methods=["GET", "POST"])
def post(postid):
    post_id = data.get_post_by_pk(postid)
    if request.method == "GET":
        comments_id = data.get_comments_by_post_id(postid)
        comments_all = len(comments_id)
        return render_template("post.html", post_id=post_id, comments_id=comments_id, comments_all=comments_all)
    else:
        name = request.form["name"]
        comment = request.form["comment"]
        data.add_comments(postid, name, comment)
        comments_id = data.get_comments_by_post_id(postid)
        comments_all = len(comments_id)
        return render_template("post.html", post_id=post_id, comments_id=comments_id, comments_all=comments_all)


@app.route("/search/")
def search():
    s = request.args.get("s")
    data_search = data.search_for_posts(s)
    len_data = len(data_search)
    return render_template("search.html", data_s=data_search, s=s, len_data=len_data)


@app.route("/users/<username>")
def users(username):
    users = data.get_posts_by_user(username)
    return render_template("user-feed.html", users=users)


@app.route("/api/posts")
def get_json_post():
    data_post = data.get_posts_all()
    return jsonify(data_post)


@app.route("/api/posts/<int:post_id>")
def get_json_post_id(post_id):
    post_id = data.get_post_by_pk(post_id)
    return jsonify(post_id)


@app.route("/bookmarks/")
def get_bookmarks():
    return render_template("bookmarks.html", all_bookmarks=data.all_bookmarks())


@app.route("/tag/<tagname>")
def get_tag(tagname):
    pass


@app.route("/bookmarks/add/<int:postid>/")
def get_post_id_add(postid):
    data.get_add_bookmarks_post_id(postid)
    return redirect("/", code=302)


@app.route("/bookmarks/remove/<int:postid>/")
def get_post_id_remove(postid):
    data.del_bookmarks(postid)
    return redirect("/bookmarks/", code=302)


if __name__ == '__main__':
    app.run(debug=True)
