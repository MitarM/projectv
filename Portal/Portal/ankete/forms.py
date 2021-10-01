from .models import Stavka, Pitanja, Otvorena_pitanja, Anketa
from django import forms

class AnketeCreateForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ["naziv_ankete", "vidljivost_ankete"]

    def __init__(self, *args, **kwargs):
        super(AnketeCreateForm, self).__init__(*args, **kwargs)
        self.fields['naziv_ankete'].label = ''
        self.fields['naziv_ankete'].widget.attrs.update(
            {
                'placeholder': 'Назив анкете',
                'class': 'form-control',
            }
        )
        for fieldname in ['vidljivost_ankete']:
            self.fields[fieldname].label = 'Уколико желите да анкета буде јавна, означите. '
        self.fields['vidljivost_ankete'].widget.attrs.update(
            {
                'class': 'form-check-input',
            }
        )

class KreiranjePitanja(forms.ModelForm):
    class Meta:
        model = Pitanja
        fields = ["pitanje", "tip_pitanja"]

    def __init__(self, *args, **kwargs):
        super(KreiranjePitanja, self).__init__(*args, **kwargs)
        for fieldname in ['pitanja']:
            self.fields[fieldname].label = 'Питања'
        for fieldname in ['tip_pitanja']:
            self.fields[fieldname].label = 'Означите ако желите отворен тип питања.'


class Glasovi(forms.ModelForm):
    class Meta:
        model = Stavka
        fields = ["glasovi"]

    def __init__(self, *args, **kwargs):
        for fieldname in ['glasovi']:
            self.fields[fieldname].label = 'Гласови'


class Otvorena_pitanja(forms.ModelForm):
    class Meta:
        model = Otvorena_pitanja
        fields = ["odgovor"]

    def __init__(self, *args, **kwargs):
        for fieldname in ['odgovor']:
            self.fields[fieldname].label = 'Упишите Ваш одговор:'
