from django import forms

class Nameform(forms.Form):
    g = [['male','male'],['female','female']]
    c = [['python','python'], ['sql','sql'],['djando','django']]
    sname = forms.CharField()
    sage = forms.IntegerField()
    password = forms.CharField(widget= forms.PasswordInput)
    address = forms.CharField(widget = forms.Textarea(attrs={'cols':5, 'rows':5}))
    gender= forms.ChoiceField(choices=g, widget= forms.RadioSelect)
    course = forms.MultipleChoiceField(choices=c, widget=forms.CheckboxSelectMultiple )