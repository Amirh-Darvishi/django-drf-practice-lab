from django import forms
from blog.models import Post

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'published_date']