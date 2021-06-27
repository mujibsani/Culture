from django import forms


class ArticleForm(forms.Form):
    give_your_keyword = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please Input your Keyword list using comma(,)','class':'form-control rounded-0', 'rows': 1, 'cols': 100}))
    article = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description', 'class':'form-control rounded-0', 'rows': 30, 'cols': 100}))


class EmailForm(forms.Form):
    give_your_url = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please Input your URL','class':'form-control rounded-0', 'rows': 1, 'cols': 100}))

