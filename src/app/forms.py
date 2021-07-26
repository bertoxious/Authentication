from django import forms
from app.models import BasicDetails, Education


class BasicDetailsForm(forms.ModelForm):

    class Meta:
        model = BasicDetails
        fields = '__all__'
        exclude = ['users']


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['users']
