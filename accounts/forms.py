from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    # user = forms.CharField(help_text='This field cannot be changed!', widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'interest', 'code_goal']
        # fields = '__all__'
        # exclude = ['user']

        