import praw
import re
import os


# Create the reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("post_replied_to.txt"):
    posts_replied_to = []
else:
    # Opens file and create list of submission ids
    with open("post_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to)) # Gets rid of empty values

subreddit = reddit.subreddit('pythonforengineers')


for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("otter", submission.title, re.IGNORECASE):
            submission.reply("Here is an \n[Otter](https://i.ytimg.com/vi/ptkytDOVFN0/maxresdefault.jpg)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)  # keep track of submissions replied to

with open("post_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")




