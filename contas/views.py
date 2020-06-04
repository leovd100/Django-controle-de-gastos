from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Transacao
from .forms import Constru_Form



# Create your views here.
def home(requests):
	data = {
		'trasacoes':['t1','t2','t3']
	}
	#data_today = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'

	data['agora'] = datetime.now().strftime('%d/%m/%Y')

	#html = '<html><body>Data e Hora atual %s</body></html>'% agora
	return render(requests, 'contas/home.html',data)



def listagem(requests):
	data = {}
	data['transacao'] = Transacao.objects.all()
	return render(requests, 'contas/lista.html',data)


def newTransfer(requests):
	data = {}
	formulario = Constru_Form(requests.POST or None)

	if formulario.is_valid():
		formulario.save()
		return redirect('url_lista')


	data['form'] = formulario
	return render(requests, 'contas/form.html',data)

def update(requests, primary):
	data = {}
	transacao = Transacao.objects.get(pk=primary)
	form = Constru_Form(requests.POST or None, instance=transacao)

	if form.is_valid():
		form.save()
		return redirect('url_lista')


	data['form'] = form
	data['obj'] = transacao
	return render(requests, 'contas/form.html',data)




def delete(requests, pk):
	transacao = Transacao.objects.get(pk=pk)
	transacao.Delete()
	return redirect('url_lista')
