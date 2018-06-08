from bs4 import BeautifulSoup
import urllib

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/4592908/c-queue-simple-example')
soup = BeautifulSoup(webpage, 'html.parser')

data = {}
question = {}
data['question'] = question

dirtyQTitle = soup.find('a', attrs={'class':'question-hyperlink'})
cleanQTitle = dirtyQTitle.text
question['title'] = cleanQTitle

for words in soup.find_all('div', attrs={'class':'postcell'}):
	cleanQBody = (words.find('div', attrs={'class':'post-text'}).text)
	userDetails = (words.find('div', attrs={'class':'user-details'}))
	asker = userDetails.find('a').text
question['body'] = cleanQBody
question['asker'] = asker

upvotes = soup.find('span',attrs={'itemprop':'upvoteCount'}).text
question['upvotes'] = upvotes
print(question['body'])

answers = []
for words in soup.find_all('div', attrs={'class':'answer'}):
	for moreWords in words.find_all('p'):
		answers.append(moreWords.text)