from bs4 import BeautifulSoup
import urllib
import pprint

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/4592908/c-queue-simple-example')
soup = BeautifulSoup(webpage, 'html.parser')

data = {}
question = {}
qComments = []

title = soup.find('a', attrs={'class':'question-hyperlink'}).text
question['title'] = title

for words in soup.find_all('div', attrs={'class':'postcell'}):
	qBody = words.find('div', attrs={'class':'post-text'}).text
	qUserDetails = words.find('div', attrs={'class':'user-details'})
	qAuthors = []
	qAuthors.append(qUserDetails.find('a').text)
	for comments in words.find_next_sibling().find_all('li', attrs={'class':'comment'}):
		qComment = {}
		qComment['comment'] = comments.find('span',attrs={'class':'comment-copy'}).text
		qComment['author'] = comments.find('a', attrs={'class':'comment-user'}).text
		qComment['upvotes'] = comments.find('div', attrs={'class':'comment-score'}).text
		qComments.append(qComment)

question['body'] = qBody
question['authors'] = qAuthors
qUpvotes = soup.find('span', attrs={'itemprop':'upvoteCount'}).text
question['upvotes'] = qUpvotes
question['comments'] = qComments

answers = []
data['answers'] = answers
answer = {}
aComments = []
answer['comments'] = aComments
for words in soup.find_all('div', attrs={'class':'answercell'}):
	answer['body'] = words.find('div', attrs={'class':'post-text'}).text
	aUserDetails = words.find('div', attrs={'class':'user-details'})
	aAuthors = []
	aAuthors.append(aUserDetails.find('a').text)
	answer['authors'] = aAuthors
	for comments in words.find_next_sibling().find_all('li', attrs={'class':'comment'}):
		aComment = {}
		aComment['comment'] = comments.find('span',attrs={'class':'comment-copy'}).text
		aComment['author'] = comments.find('a', attrs={'class':'comment-user'}).text
		aComment['upvotes'] = comments.find('div', attrs={'class':'comment-score'}).text
		aComments.append(aComment)
	answers.append(answer)