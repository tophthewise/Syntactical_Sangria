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
	# must be casted in a list
	submitted_test.append( data2[455][data_labels[1]])
	submitted_test.append( data2[455][data_labels[2]])
	submitted_test.append( data2[455][data_labels[3]])
	submitted_test.append( data2[455][data_labels[4]])


	# print(submitted_test)

	stoplist = set('for a of the and to in'.split())
	# set the ads into proper format 
	texts = [[word for word in text.split() if word not in stoplist]for text in submitted_test]
	# from collections import defaultdict
	# frequency = defaultdict(int)
	# for text in texts:
	# 	for token in text:
	# 		frequency[token] += 1
	# texts = [[token for token in text if frequency[token] > 1]
	# 		 for text in texts]
	# from pprint import pprint 
	# # pprint(texts)
	# print(texts)
	# texts[i][len(texts[i])-1] is the last word of the list that we are dealing with 

	texts[0][0] = texts[0][0][2:]
	texts[0][len(texts[0])-1] = texts[0][len(texts[0])-1][:len(texts[0][len(texts[0])-1])-2]
	
	texts[1][0] = texts[1][0][2:]
	texts[1][len(texts[1])-1] = texts[1][len(texts[1])-1][:len(texts[1][len(texts[1])-1])-2]
	
	texts[2][0] = texts[2][0][2:]
	texts[2][len(texts[2])-1] = texts[2][len(texts[2])-1][:len(texts[2][len(texts[2])-1])-2]
	
	texts[3][0] = texts[3][0][2:]
	texts[3][len(texts[3])-1] = texts[3][len(texts[3])-1][:len(texts[3][len(texts[3])-1])-2]
	print(texts)

	dictionary = corpora.Dictionary(texts)
	# puts the stuff in correct form
	print(dictionary)
	submission = data2[455][data_labels[0]]
	
	submission= submission[2:len(submission)-3]
	print(submission)
	new_vec = dictionary.doc2bow(submission.split())
	print(submission.split())
	# print(new_vec)
	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	print(corpus)
	print(tfidf[new_vec])


			# print(data_labels[0])
# stoplist = set('for a of the and to in'.split())
# texts = [[word for word in document.lower().split() if word not in stoplist]
# 	for document in documents]
# print(texts);