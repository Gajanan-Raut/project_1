from django import forms
from shoppingapp.models import student

class emp(forms.Form):
    emp_name=forms.CharField()
    emp_address=forms.CharField()
    emp_roll=forms.IntegerField()


class stus(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    age=forms.IntegerField()
    marks=forms.IntegerField()
    

class stud(forms.ModelForm):
    names=forms.CharField()
    age=forms.IntegerField()
    address=forms.CharField()

    class Meta:
        model=student
        fields="__all__"
        
    
