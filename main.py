import webparser
import output

url = input('input here: ')

data_parsed = webparser.parseIt(url)
output.writeJSON(data_parsed)