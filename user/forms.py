from django import forms


class BlogUserForm(forms.Form):
    username = forms.CharField(label='ID', max_length=30, label_suffix='')
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(), label_suffix='')
    password2 = forms.CharField(label='Password Check', max_length=30, widget=forms.PasswordInput(),
                               label_suffix='')
    name = forms.CharField(label='Name', max_length=30, label_suffix='')
    name = forms.CharField(label='Phonenumber', max_length=30, label_suffix='')
    sex = forms.ChoiceField(label='Sex', choices=(('m', 'Male'), ('f', 'Female')),
                            label_suffix='')

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            cleaned_data['error_messages'] = 'Passwords are not same'
        return cleaned_data
