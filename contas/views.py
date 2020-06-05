from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Transacao
from .forms import Constru_Form



# Create your views here.
def home(request):
	data = {
		'trasacoes':['t1','t2','t3']
	}
	#data_today = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'

	data['agora'] = datetime.now().strftime('%d/%m/%Y')

	#html = '<html><body>Data e Hora atual %s</body></html>'% agora
	return render(request, 'contas/home.html',data)



def listagem(request):
	data = {}
	data['transacao'] = Transacao.objects.all()
	return render(request, 'contas/lista.html',data)


def newTransfer(request):
	data = {}
	formulario = Constru_Form(request.POST or None)

	if formulario.is_valid():
		formulario.save()
		return redirect('url_lista')


	data['form'] = formulario
	return render(request, 'contas/form.html',data)

def update(request, primary):
	data = {}
	transacao = Transacao.objects.get(pk=primary)
	form = Constru_Form(request.POST or None, instance=transacao)

	if form.is_valid():
		form.save()
		return redirect('url_lista')


	data['form'] = form
	data['obj'] = transacao
	return render(request, 'contas/form.html',data)



def delete(request, pk):
	if form.is_valid():
		Transacao.objects.get(pk=pk).delete()
	return redirect('url_lista')