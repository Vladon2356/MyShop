from django import forms
from .models import ToOrder


class ToOrderForm(forms.ModelForm):
    class Meta:
        model = ToOrder
        fields = ('type', 'material', 'size', 'description', 'telephone_number')
        labels = {
            'type': 'Категорія товару',
            'material': 'Матеріал з якого буде виготовлено виріб',
            'size': 'Розмір виробу',
            'description': 'Більш детальний опис Ваших бажань',
            'telephone_number': 'Ваш номер (щоб ми могли з Вами зв’язатись)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control',
                                                       'style': 'width: 20%;'}),
        }
