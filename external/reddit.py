import praw
import requests


class Reddit(object):

    def __init__(self,
                 reddit_secret, reddit_id,
                 reddit_username, reddit_password):
        self.secret = reddit_secret
        self.id = reddit_id
        self.username = reddit_username
        self.password = reddit_password
        self.user_agent = 'Caffeinated Eyes Comment taker'

    def praw(self):
        reddit = praw.Reddit(
                 client_id=self.id,
                 client_secret=self.secret,
                 user_agent=self.user_agent,
                 username=self.username,
                 password=self.password)
        return reddit

    def get_comment_body(self, comment_id):
        reddit = self.praw()
        comment = reddit.comment(id=comment_id)
        submission = comment.submission
        submission = {
                "title": submission.title,
                "slug": submission.id}
        prompt = {
                "permalink": "https://reddit.com" + comment.permalink(),
                "slug": comment_id,
                "author": comment.author.__str__(),
                "story": comment.body
                }
        submission['prompt'] = prompt
        return submission

    def post_comment(self, payload={}):
        url = ""
        payload = {
                "submission": {
                    "title": payload["title"],
                    "slug": payload["slug"],
                    },
                "slug": payload["prompt"]["slug"],
                "author": payload["prompt"]["author"],
                "story": payload["prompt"]["story"]
                }
        r = requests.post(url, payload)
        return r
