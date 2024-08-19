from django import forms
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

# Custom login form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','mobile','std_id','department')
        labels = {
            'fullname':'Full Name',
            'std_id':'STD. ID'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        self.fields['mobile'].required = False