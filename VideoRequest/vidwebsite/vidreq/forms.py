from django import forms

class VideoForms(forms.Form):

    vidname = forms.CharField(max_length=20,widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'inputName',
                'placeholder':'Name'
            }
    ))

    viddesc = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows':'5',
            'id':'comment',
            'placeholder':'Comment'
        }
    ))
