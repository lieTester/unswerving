from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from lander_portal.models import *


class AddCourse(forms.ModelForm):
    class Meta:
        model = Courses_Exams
        fields = '__all__'


class AddSubject(forms.ModelForm):
    class Meta:
        model = Subjects_toStudy
        fields = '__all__'


class AddTopics(forms.ModelForm):
    class Meta:
        model = Topics_comes
        fields = '__all__'


class UploadFile(forms.ModelForm):
    class Meta:
        model = ImageUplaod
        fields = '__all__'


class AddorUpdateQuestion(forms.ModelForm):
    class Meta:
        model = Question_data
        fields = ['Exam_Id', 'Topic_Id', 'Creater_Id', 'Question_detail', 'Question_Options', 'Question_Correct_Option',
                  'Question_Ans_Explain']


class AddorUpdateArticle(forms.ModelForm):
    class Meta:
        model = Article_data
        fields = '__all__'


class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'user_log'

        self.fields['email'].widget.attrs['class'] = 'email_log'
        self.fields['email'].widget.attrs['required'] = 'required'

        self.fields['password1'].widget.attrs['class'] = 'pass1_log'

        self.fields['password2'].widget.attrs['class'] = 'pass2_log'
