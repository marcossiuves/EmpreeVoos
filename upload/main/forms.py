from django import forms

QUANTIDADE_AGENDAMENTOS = []

for i in range(1, 11):
    QUANTIDADE_AGENDAMENTOS.append((i, str(i)))


class AgendamentosForm(forms.Form):

    quantidade = forms.TypedChoiceField(
        choices=QUANTIDADE_AGENDAMENTOS, coerce=int)

    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)
