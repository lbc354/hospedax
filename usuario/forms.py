from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class LoginForm(AuthenticationForm):
    # O Django internamente espera "username"
    # Mesmo usando email como login, o campo deve se chamar username
    username = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email and password:
            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                raise forms.ValidationError("E-mail não encontrado.")

            if not user.check_password(password):
                raise forms.ValidationError("E-mail e/ou senha incorretos.")

            if not user.is_active:
                raise forms.ValidationError("Esta conta está desativada. Se isto for um erro, entre em contato.")

            self.user_cache = user
            return self.cleaned_data

        return super().clean()


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")

        return email


class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["email", "is_active", "is_staff"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        qs = Usuario.objects.filter(email=email).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Email já está em uso.")

        return email
