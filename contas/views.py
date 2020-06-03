from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(requests):
	data = {}
	data['agora'] = datetime.datetime.now()
	#html = '<html><body>Data e Hora atual %s</body></html>'% agora
	return render(requests, 'contas/home.html',data)

