from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Courses_Exams)
admin.site.register(Subjects_toStudy)
admin.site.register(Topics_comes)
admin.site.register(Question_data)
admin.site.register(Article_data)
admin.site.register(ImageUplaod)
admin.site.register(Tags_toMatch)
