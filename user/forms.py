from django import forms


class BlogUserForm(forms.Form):
    username = forms.CharField(label='ID', max_length=30, initial='아이디 집어넣어..')
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Check', max_length=30, widget=forms.PasswordInput(),
                               )
    name = forms.CharField(label='Name', max_length=30)
    phonenumber = forms.CharField(label='Phonenumber', max_length=30)
    sex = forms.ChoiceField(label='Sex', choices=(('m', 'Male'), ('f', 'Female')),
                            )

    error_css_class = 'error'
    required_css_class = 'required'

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password1', 'Passwords are not same')
        return cleaned_data
