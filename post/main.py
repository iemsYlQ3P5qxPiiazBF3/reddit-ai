import praw
import time
import subprocess

reddit = praw.Reddit(client_id='client_id', client_secret='client_secret', password='password', user_agent='user_agent', username='username')
sub = reddit.subreddit('r_all_ai')
def getpost():
	posts = reddit.subreddit('all').new(limit=10)
	for post in posts:
		with open('/home/user/ai/all.txt', 'a') as f:
			f.write(post.title + "\n" + post.selftext)

while True:
	title = subprocess.getoutput("cd /home/user/ai;gen all.txt 10|sed 's/u\//u_/g' 2>/dev/null")
	text = subprocess.getoutput("cd /home/auser/ai;gen all.txt 5000|sed 's/u\//u_/g' 2>/dev/null")
	sub.submit(title,selftext=text)
	getpost()
	time.sleep(200)
