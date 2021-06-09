import praw
import time
import subprocess
import sys
previous_id = "0"
reddit = praw.Reddit(client_id='client_id', client_secret='client_secret', password='password', user_agent='user_agent', username='username')

previous_id = "0"
def search():
	for results in reddit.subreddit('all').comments():
		global previous_id
		body = results.body
		body = body.lower()
		comment_id = results.id
		if comment_id == previous_id:
			print("id " + comment_id + " already replied.")
			return "Error"
		found = body.find('u/username')
		if found != -1:
			previous_id = comment_id
			try:
				results.reply(subprocess.getoutput('cd /home/username/ai;gen all.txt 555|sed "s/u\//u_/g"'))
				print("\033[38;05;128;128;255mReplied to " + comment_id + "\033[0m")
			except:
				print("error??????")
				break

while 1:
	search()
	time.sleep(5)