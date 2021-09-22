from . import models

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrationOForm(UserCreationForm):

    # username = forms.CharField(
    #     label="Корисничко име",
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #         }
    #     )
    # )

    password1 = forms.CharField(
        label="Лозинка",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                "class": "form-control",
                "placeholder": 'Унесите лозинку'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label="Потврда лозинке",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                "class": "form-control",
                "placeholder": 'Поновите лозинку'
            }
        ),
        strip=False,
        help_text="",
    )

    naziv = forms.CharField(
        label="Назив",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    opis = forms.CharField(
        label="Опис",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "4"
            }
        )
    )

    pib = forms.CharField(
        label="ПИБ",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    delatnost = forms.CharField(
        label="Делатност",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    sajt = forms.CharField(
        label="Сајт",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    telefon = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    sediste = forms.CharField(
        label="Место",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    ulica = forms.CharField(
        label="Улица",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = User
        fields = [ "username", "email"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def save(self, commit=True):
        user = super(RegistrationOForm, self).save(commit)
        # user.is_staff = True
        # user.save()
        naziv = self.cleaned_data.get("naziv")
        pib = self.cleaned_data.get("pib")
        opis = self.cleaned_data.get("opis")
        delatnost = self.cleaned_data.get("opis")
        sajt = self.cleaned_data.get("delatnost")
        telefon = self.cleaned_data.get("telefon")
        sediste = self.cleaned_data.get("sediste")
        ulica = self.cleaned_data.get("ulica")

        organizacija = models.Organizacija(user=user, naziv=naziv, pib=pib, opis=opis, sajt=sajt, telefon=telefon, sediste=sediste, ulica=ulica)
        if commit:
            organizacija.save()

        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationOForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].label = 'Корисничко име'

        for fieldname in ['email']:
            self.fields[fieldname].label = 'Имејл'


class RegistrationVForm(UserCreationForm):

    password1 = forms.CharField(
        label="Лозинка",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                "class": "form-control",
                "placeholder": 'Унесите лозинку'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label="Потврда лозинке",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                "class": "form-control",
                "placeholder": 'Поновите лозинку'
            }
        ),
        strip=False,
        help_text="",
    )

    # ime = forms.CharField(
    #     label="Име",
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #         }
    #     )
    # )
    #
    # prezime = forms.CharField(
    #     label="Презиме",
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #         }
    #     )
    # )

    datum_rodjenja = forms.DateField(
        label="Датум рођења",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            },
        )
    )



    telefon = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    POLOVI = (
        (1, 'Мушки'),
        (2, 'Женски'),
        (3, 'Друго, тј. треће'),
    )

    pol = forms.ChoiceField(
        label="Пол",
        choices=POLOVI,
    )

    slika = forms.ImageField(
        label="Слика",
    )

    cv = forms.FileField(
        label="Резиме",
        # widget=forms.FileField(
        #     attrs={
        #         "class": "form-control",
        #     }
        # )
    )

    #
    # mesto = forms.CharField(
    #     label="Место",
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #         }
    #     )
    # )
    #
    # ulica = forms.CharField(
    #     label="Улица",
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #         }
    #     )
    # )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        widgets = {
            # "username": forms.EmailInput(
            #     attrs={
            #         "class": "form-control"
            #     }
            # ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def save(self, commit=True):
        user = super(RegistrationVForm, self).save(commit=False)
        user.username = user.email
        user.save()
        datum_rodjenja= self.cleaned_data.get("datum_rodjenja")
        telefon = self.cleaned_data.get("telefon")
        pol = self.cleaned_data.get("pol")
        slika = self.cleaned_data.get("slika")
        cv = self.cleaned_data.get("cv")

        # mesto = self.cleaned_data.get("sediste")
        # ulica = self.cleaned_data.get("ulica")

        volonter = models.Volonter(user=user, datum_rodjenja=datum_rodjenja, telefon=telefon, pol=pol, slika=slika, cv=cv)
        if commit:
            volonter.save()

        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationVForm, self).__init__(*args, **kwargs)

        for fieldname in ['email']:
            self.fields[fieldname].label = 'Имејл'

        self.fields['first_name'].label = 'Име'
        self.fields['last_name'].label = 'Презиме'
        self.fields['pol'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

        self.fields['slika'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

        self.fields['cv'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

