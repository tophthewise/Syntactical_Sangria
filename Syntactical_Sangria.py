from gensim import corpora, models, similarities
import csv

import csv 
with open('Boost1.csv', 'r') as csvfile:
	data_in = csv.reader(csvfile, delimiter = ',',quotechar = '|')
	data1 = []
	data2 = []
	data_labels = []
	for row in data_in:

		data1.append(row)

	data_labels  = data1[0]
	for i in range(1,len(data1)):
		obj= {}
		for j in range(len(data_labels)):
			obj[data_labels[j]] = data1[i][j]
		data2.append(obj)


	submitted_test=[]
	submitted_test.append( [data2[200][data_labels[2]]])
	submitted_test.append( [data2[200][data_labels[1]]])
	# print(submitted_test)

	stoplist = set('for a of the and to in'.split())
	texts = [[word for word in submitted_test if word not in stoplist]for text in submitted_test]
	texts[0] = texts[0][2:]
	texts[len(texts)-1] = texts[len(texts)-1][:len(texts[len(texts)-1])-2]
	print(texts)
	dictionary = corpora.Dictionary(texts)
	# print(dictionary)

			# print(data_labels[0])
# stoplist = set('for a of the and to in'.split())
# texts = [[word for word in document.lower().split() if word not in stoplist]
# 	for document in documents]
# print(texts);