from bs4 import BeautifulSoup
import urllib
import pprint
import json

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/4592908/c-queue-simple-example')
soup = BeautifulSoup(webpage, 'html.parser')

data = {}
question = {}
data['question'] = question
qComments = []

title = soup.find('a', attrs={'class':'question-hyperlink'}).text
question['title'] = title

for words in soup.find_all('div', attrs={'class':'postcell'}):
	qBody = words.find('div', attrs={'class':'post-text'}).text
	qAuthors = []
	for users in words.find_all('div', attrs={'class':'user-details'}):
		qAuthors.append(users.find('a').text)
	qUpvotes = words.find_previous_sibling().find('span', attrs={'itemprop':'upvoteCount'}).text
	for comments in words.find_next_sibling().find_all('li', attrs={'class':'comment'}):
		qComment = {}
		qComment['comment'] = comments.find('span',attrs={'class':'comment-copy'}).text
		qComment['author'] = comments.find('a', attrs={'class':'comment-user'}).text
		qComment['upvotes'] = comments.find('div', attrs={'class':'comment-score'}).text
		qComments.append(qComment)

question['body'] = qBody
question['authors'] = qAuthors
question['upvotes'] = qUpvotes
question['comments'] = qComments

answers = []
data['answers'] = answers
answer = {}

for words in soup.find_all('div', attrs={'class':'answercell'}):
	answer = {}
	aComments = []
	aBody = words.find('div', attrs={'class':'post-text'}).text
	aAuthors = []
	for users in words.find_all('div', attrs={'class':'user-details'}):
		aAuthors.append(users.text)
	aUpvotes = words.find_previous_sibling().find('span', attrs={'itemprop':'upvoteCount'}).text
	for comments in words.find_next_sibling().find_all('li', attrs={'class':'comment'}):
		aComment = {}
		aComment['comment'] = comments.find('span', attrs={'class':'comment-copy'}).text
		aComment['author'] = comments.find('a', attrs={'class':'comment-user'}).text
		aComment['upvotes'] = comments.find('div', attrs={'class':'comment-score'}).text
		aComments.append(aComment)
	answer['body'] = aBody
	answer['authors'] = aAuthors
	answer['upvotes'] = aUpvotes
	answer['comments'] = aComments
	answers.append(answer)

json.dumps(data)