from django.contrib import admin
from .models import CustomUser, Subject, Question, Result

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'student_id', 'email']  # Add student_id and email
    search_fields = ['username', 'student_id']  # Allow searching by username and student_id
    list_filter = ['role']  # Filter users by role (admin/student)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']  # Allow searching by subject name

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['subject', 'question_text', 'question_type', 'difficulty', 'options_display', 'correct_answer']
    search_fields = ['question_text', 'subject__name', 'question_type']
    list_filter = ['difficulty', 'subject__name']  # Assuming 'name' is the field in Subject model

    def options_display(self, obj):
        return ", ".join(f"{key}: {value}" for key, value in obj.options.items()) if obj.options else "No options"
    options_display.short_description = 'Options'

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'marks', 'grade', 'correct_answers', 'total_questions']  # Added relevant fields
    search_fields = ['user__username', 'subject__name']  # Search by username and subject name
    list_filter = ['grade']  # Filter results by grade
