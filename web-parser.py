from bs4 import BeautifulSoup
import urllib
import numpy as np

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/3477741/why-does-c-require-a-cast-for-malloc-but-c-doesnt')
soup = BeautifulSoup(webpage, 'html.parser')
question = []
answers = []
users = []

dirtyQTitle = soup.find('a', attrs={'class':'question-hyperlink'})
cleanQTitle = dirtyQTitle.text.strip()
question.append(cleanQTitle)
#print(cleanQuestion)

dirtyQBody = soup.find('div', 'post-text')
cleanQBody = dirtyQBody.text.strip()
question.append(cleanQBody)
#print(cleanQdesc)

dirtyUsers = soup.find_all('div', attrs={'class':'user-details'})
for j in dirtyUsers:
	users.append(j.text.strip())
#print(users)


dirtyAnswers = soup.find_all('div', attrs={'class':'answer'})
for words in dirtyAnswers:
	answers.append(words.text.strip())
#print(answers)