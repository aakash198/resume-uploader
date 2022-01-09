from os import name
from django import forms
from django.forms import widgets
from .models import resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
]
JOB_CITY_CHOICE=[
    ('Delhi','delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Dhanbad','Dhanbad'),
    ('Banglone','Banglore')
]
class resumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred job locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=resume
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels={'name':'Full Name','dob' :'Date of Birth','pin': 'Pin Code','mobile': 'Mobile No.','email':'Email ID','profile_image': 'Profile Image', 'my_file':'Document'}
        widgets={  # here we are using bootstrap class for looking like good in one by one box
            'name':forms.TextInput(attrs={'class':'form-control'}),  
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        } 