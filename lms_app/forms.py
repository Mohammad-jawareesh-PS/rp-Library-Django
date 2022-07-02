from django import forms
from .models import *
class CategoryForm(forms.ModelForm):
    class Meta:
         model = Category
         fields = '__all__'
         widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            
         }

class BookForm(forms.ModelForm):
     class Meta:
         model = Book
         fields = '__all__'
         widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class':'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class':'form-control'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day' : forms.NumberInput(attrs={'class':'form-control', 'id':'rpd'}),
            'retal_period' : forms.NumberInput(attrs={'class':'form-control' ,'id':'rp'}),
            'total_rental' : forms.NumberInput(attrs={'class':'form-control' ,'id':'tr'}),
            'active' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
         }

# [
#              'title',
#              'author',
#              'photo_book',
#              'photo_author',
#              'pages',
#              'price',
#              'retal_price_day',
#              'retal_period',
#              'active',
#              'status',
#              'category',
#          ]