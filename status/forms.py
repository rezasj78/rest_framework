from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'img',
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == '':
            content = None
        img = data.get('img', None)
        if content is None and img is None:
            raise forms.ValidationError('content or image is required')
        return super().clean(*args, **kwargs)
