from django import forms
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 rounded-md border border-gray-600 bg-white text-black"
            }),
            "price": forms.NumberInput(attrs={
                "class": "w-full px-3 py-2 rounded-md border border-gray-600 bg-white text-black"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-3 py-2 rounded-md border border-gray-600 bg-white text-black"
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "w-full px-3 py-2 rounded-md border border-gray-600 bg-white text-black"
            }),
            "category": forms.Select(attrs={
                "class": "w-full px-3 py-2 rounded-md border border-gray-600 bg-white text-black"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "rounded text-green-600 focus:ring-green-500"
            }),
        }
