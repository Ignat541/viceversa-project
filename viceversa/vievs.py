from django.shortcuts import render

def tabela(request):
	return render(request, 'home.html')