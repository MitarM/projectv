from django import forms
from .models import Oglas

class Forma_postavljanja_oglasa(forms.ModelForm):
    class Meta:
        model = Oglas

        fields = ["naslov", "tekst", "vidljivost",
                  #"datum",
                  ];

        # vidljivost = forms.ChoiceField(
        #     label="Видљивост"
        # )

        # exclude

        # widgets = {
        #    "datum": forms.DateTimeField(
        #        label= "Датум",
        #
        #  )
        #  }


    def __init__(self, *args, **kwargs):
        super(Forma_postavljanja_oglasa, self).__init__(*args, **kwargs)
        for fieldname in ['naslov']:
            self.fields[fieldname].label = 'Наслов'
        for fieldname in ['tekst']:
            self.fields[fieldname].label = 'Текст'
        for fieldname in ['vidljivost']:
            self.fields[fieldname].label = 'Видљивост'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # for fieldname in ['datum']:
        #    self.fields[fieldname].label = 'Датум'
        # for fieldname in ['vidljivost']:
        #     self.fields[fieldname].label = 'Видљивост'

        # widgets = {
        #   "datum": forms.DateTimeField(
        #     attrs={
        #        "class": "form-control", 'type': 'date'
        #    }
        # )
        # }

        # widgets = {
        # "datum_isteka_oglasa": forms.date(
        #     attrs={
        #         "class": "form-control"
        #     }
        # )
        # }

        # widgets = {
        #     "vidljivost": forms.MultipleChoiceField(
        #         attrs={
        #             "class": "form-control"
        #         }
        #     )
        # }