from django import forms
from myapp.models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta():
        model = Feedback
        fields = '__all__'
