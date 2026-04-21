from django import forms
from .models import Destino


class DestinoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Destino
        fields = ["titulo", "descricao", "localizacao", "preco", "imagem"]

        labels = {
            "titulo": "Título do destino",
            "descricao": "Descrição",
            "localizacao": "Localização",
            "preco": "Preço (R$)",
            "imagem": "Imagem",
        }

        help_texts = {"imagem": "Apenas PNG, JPG ou JPEG."}

        widgets = {
            "titulo": forms.TextInput(attrs={}),
            "descricao": forms.Textarea(attrs={"rows": 2}),
            "localizacao": forms.TextInput(attrs={}),
            "preco": forms.NumberInput(attrs={}),
            "imagem": forms.ClearableFileInput(attrs={}),
        }
