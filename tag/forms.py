from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from tag.models import TagForm

class TagModelForm(ModelForm):
    class Meta:
        model = TagForm
        fields = ['toTag','message']

    def __init__(self, userId, *args, **kwargs):
        super(TagModelForm, self).__init__(*args, **kwargs)
        self.fields['toTag'].label = "User to Tag"
        self.fields['toTag'].queryset = User.objects.exclude(username=userId) # Excludes the current user from the dropdown so they can't tag themselves
        self.fields['message'].label = "Add a message!"