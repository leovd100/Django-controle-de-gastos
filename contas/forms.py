from django.forms import ModelForm
from .models import Transacao

class  Constru_Form (ModelForm):
	class Meta:
		model = Transacao
		fields = ['data','descricao','valor','categoria','observacoes'] 