from cProfile import label
from django import forms
from ALL_FOR_ONE.models import SignUp, Blog, Comments, Contact

# class adminform(forms.ModelForm):
#     admin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name', 'class':'form-control','type':'text','id':'admin'}))
#     password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Password', 'class':'form-control', 'type':'password','id':'Password'}))

#     class Meta:
#         model = admin_login
#         fields = '__all__'

# class SignUpForm(forms.ModelForm):
#     Name = forms.CharField(max_length=50)
#     Email = forms.EmailField()
#     Password = forms.CharField(max_length=50)

#     class Meta:
#         model = SignUp
#         fields = '__all__'

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ('U_Name', 'Title', 'Detail', 'File', 'U_id')
        
# class Profile(forms.ModelForm):
#     class Meta:
#         model = SignUp
#         fields = ('Pro_Img', 'Name', 'Email', 'Password', 'Phone', 'Address')