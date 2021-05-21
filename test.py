count = 0
search_word = 'many'

with open('words.txt') as file:
	data = file.read()

	splitted_data  = data.split()

	for word in splitted_data:
		if word == search_word:
			count += 1
print(count)