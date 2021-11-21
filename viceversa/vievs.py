from django.shortcuts import render

def tabela(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	number_of_words = len(words)
	reversed_text = user_text[::-1]
	print(reversed_text)
	return render(request, 'reverse.html', {'usertext': user_text,
		'reversedtext':reversed_text, 'number_of_words': number_of_words})

# def domzad(request):
	# user_text = user_text.split()
	# counter = 0

	# for word in user_text:
	# 	counter += 1

	# return render(request, 'domzad.py')
