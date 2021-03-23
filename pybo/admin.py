from django.contrib import admin

# Edit

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question,QuestionAdmin)