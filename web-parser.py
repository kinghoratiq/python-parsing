from bs4 import BeautifulSoup
import urllib
import numpy as np

webpage = urllib.request.urlopen('https://stackoverflow.com/questions/3477741/why-does-c-require-a-cast-for-malloc-but-c-doesnt')
soup = BeautifulSoup(webpage, 'html.parser')
question = []
answers = []
qa_array = []

dirtyQTitle = soup.find('a', attrs={'class':'question-hyperlink'})
cleanQTitle = dirtyQuestion.text.strip()
question.append(cleanQTitle)
#print(cleanQuestion)
dirtyQBody = soup.find("div", "post-text")
cleanQBody = dirtyQdesc.text.strip()
question.append(cleanQBody)
#print(cleanQdesc)

dirtyAnswers = soup.find_all()