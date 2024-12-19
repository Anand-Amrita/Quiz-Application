from django import forms
from .models import CustomUser, Subject

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'student_id', 'age', 'school', 'class_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RemoveStudentForm(forms.Form):
    student_id = forms.CharField(max_length=100)

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if not CustomUser.objects.filter(student_id=student_id, role='student').exists():
            raise forms.ValidationError("Student ID does not exist.")
        return student_id

