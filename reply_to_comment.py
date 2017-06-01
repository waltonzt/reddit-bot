import praw
import re
import os


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    # Opens file and create list of submission ids
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))   # Gets rid of empty values


for comment in subreddit.stream.comments():
    if comment.id not in comments_replied_to:
        if re.search("otters are lame", comment.body, re.IGNORECASE):
            comment.reply("[Otters Rock](http://68.media.tumblr.com/7399e636f0a16846ad9dc4fdb8dbb7c7/tumblr_" +
                          "onfy2qT8lO1w5irhpo1_500.jpg)")
            comments_replied_to.append(comment.id)  # keep track of submissions replied to


with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")