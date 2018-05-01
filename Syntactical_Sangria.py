from gensim import corpora, models, similarities
import numbers
import csv

totalCount = 0
hitCount = 0

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

	file = open("textfile.txt","w")

	for i in range(0,len(data2)):
		for j in range(0,24,5):
			submitted_test=[]
			# must be casted in a list
			submitted_test.append( data2[i][data_labels[j]])
			submitted_test.append( data2[i][data_labels[j+1]])
			submitted_test.append( data2[i][data_labels[j+2]])
			submitted_test.append( data2[i][data_labels[j+3]])
			submitted_test.append( data2[i][data_labels[j+4]])



	# print(submitted_test)

			stoplist = set('for a of the and to in'.split())
			# set the ads into proper format
			texts = [[word for word in text.split() if word not in stoplist]for text in submitted_test]
			texts2print = [[word for word in text.split()] for text in submitted_test]

			texts2print[0][0] = texts2print[0][0][2:]
			texts2print[0][len(texts2print[0]) - 1] = texts2print[0][len(texts2print[0]) - 1][:len(texts2print[0][len(texts2print[0]) - 1]) - 2]


			# cleaned text
			texts[0][0] = texts[0][0][2:]
			texts[0][len(texts[0])-1] = texts[0][len(texts[0])-1][:len(texts[0][len(texts[0])-1])-2]

			texts[1][0] = texts[1][0][2:]
			texts[1][len(texts[1])-1] = texts[1][len(texts[1])-1][:len(texts[1][len(texts[1])-1])-2]

			texts[2][0] = texts[2][0][2:]
			texts[2][len(texts[2])-1] = texts[2][len(texts[2])-1][:len(texts[2][len(texts[2])-1])-2]

			texts[3][0] = texts[3][0][2:]
			texts[3][len(texts[3])-1] = texts[3][len(texts[3])-1][:len(texts[3][len(texts[3])-1])-2]

			texts[4][0] = texts[4][0][2:]
			texts[4][len(texts[4]) - 1] = texts[4][len(texts[4]) - 1][:len(texts[4][len(texts[4]) - 1]) - 2]
			# ]print(texts)
			# this vv should have all the words in the entirety of the data set not just suggestions because if not some of the words that show up in the submitted wont get accounted for, and will give us a "better" statistic but wont give us an accurate statistic
			if texts[0][0] == "NULL":
				continue

			##Basic comparison
			totalCount +=1
			if texts[0][0] == texts[1][0]:
				hitCount += 1
			elif texts[0][0] == texts[2][0]:
				hitCount += 1
			elif texts[0][0] == texts[3][0]:
				hitCount += 1
			elif texts[0][0] == texts[4][0]:
				hitCount += 1

			dictionary = corpora.Dictionary(texts)
			# print(dictionary.token2id)
			# puts the stuff in correct form
			# print(dictionary)
			submission = data2[i][data_labels[j]]
			submission= submission[2:len(submission)-2]
			m = submission.split()
			# print(m)
			# print(dictionary.token2id)
			new_vec = dictionary.doc2bow(m)
			if new_vec ==[]:
				continue
			# print(new_vec)
			corpus = [dictionary.doc2bow(text) for text in texts]
			tfidf = models.TfidfModel(corpus)
			# print(corpus)
			sim_arr=tfidf[new_vec]
			# print(sim_arr)
			if sim_arr ==[]:
				continue
			from functools import reduce
			f = lambda a,b: a + b[1] if (isinstance(a,numbers.Number)) else a[1]+b[1]
			final_sim = reduce(f,sim_arr)
			if(str(final_sim) == "(0, 1.0)"):
				final_sim = 1
			# print(" ".join(texts[0]), final_sim)
			x = " ".join(texts2print[0])
			x = x +","+str(final_sim) + "\n"
			file.write(x)

percentage = hitCount/totalCount
file.write("hitCount:"+ str(percentage))
		# print(data_labels[0])
# stoplist = set('for a of the and to in'.split())
# texts = [[word for word in document.lower().split() if word not in stoplist]
# 	for document in documents]
# print(texts);