from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=55, help_text="Please enter a category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Category
		fields = ('name', )

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter a page title.")
	url = forms.URLField(max_length=255, help_text="Enter the page URL.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		if url and not url.startswith("http://"):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data

	class Meta:
		model = Page
		# Instead of entering fields to include, we can...
		# exclude the foriegn key.
		exclude = ('category', )

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

