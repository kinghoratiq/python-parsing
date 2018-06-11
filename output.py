def writeJSON(data):
	json_data = open('stackoverflow.json','w')
	json_data.write(data)
	json_data.close()