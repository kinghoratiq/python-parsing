from bs4 import BeautifulSoup
import urllib

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/4592908/c-queue-simple-example')
soup = BeautifulSoup(webpage, 'html.parser')

data = {}
question = {}
data['question'] = question

dirtyTitle = soup.find('a', attrs={'class':'question-hyperlink'})
cleanTitle = dirtyTitle.text
question['title'] = cleanTitle

for words in soup.find_all('div', attrs={'class':'postcell'}):
	qCleanBody = words.find('div', attrs={'class':'post-text'}).text
	qUserDetails = words.find('div', attrs={'class':'user-details'})
	qAuthors = []
	qAuthors.append(qUserDetails.find('a').text)
question['body'] = qCleanBody
question['authors'] = qAuthors
qUpvotes = soup.find('span', attrs={'itemprop':'upvoteCount'}).text
question['upvotes'] = qUpvotes

qComments = []
question['comments'] = qComments
for words in soup.find_all('div', attrs={'class':'question'}):
	qComment = {}
	for stuff in words.find_all('span', attrs={'class':'comment-copy'}):
		qComment['comment'] = stuff.text
		qComments.append(qComment)
	for names in words.find_all('div', attrs={'class':'comment-body'}):
		qComment['author'] = names.find('a').text
	for votes in words.find_all('div', attrs={'class':'js-comment-actions'}):
		qComment['upvotes'] = votes.find('div', attrs={'class':'comment-score'}).text
	qComments.append(qComment)

answers = []
data['answers'] = answers
for stuff in soup.find_all(id='answers'):
	answer = {}
	for words in soup.find_all('div', attrs={'class':'answercell'}):
		answer['body'] = words.find('div', attrs={'class':'post-text'}).text
		aUserDetails = words.find('div', attrs={'class':'user-details'})
		aAuthors = []
		aAuthors.append(aUserDetails.find('a').text)
		answer['authors'] = aAuthors
	for votes in stuff.find_all('span', attrs={'itemprop':'upvoteCount'}):
		answer['upvotes'] = votes.text
	answers.append(answer)