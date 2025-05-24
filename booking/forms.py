from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Reservation

class UserRegisterForm(forms.ModelForm):
    nom = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput) 
    password_confirm = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']   

    def clean_email(self):
        email = self.cleaned_data.get('email')       
        if User.objects.filter(email=email).exists():   
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def clean(self):
        cleaned_data = super().clean() 
        pwd = cleaned_data.get("password")
        pwd_confirm = cleaned_data.get("password_confirm")
        if pwd and pwd_confirm and pwd != pwd_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.") 
        return cleaned_data

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        user = User.objects.filter(email=email).first()
        if user is None:
            raise forms.ValidationError("Utilisateur non trouvé.")

        user_auth = authenticate(username=user.username, password=password)
        if not user_auth:
            raise forms.ValidationError("Mot de passe incorrect.")

        cleaned_data['user'] = user_auth
        return cleaned_data

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }
