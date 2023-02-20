from django.contrib import admin

# Register your models here.

from bt.models import Teacher

class TeacherAdmin (admin.ModelAdmin):
    list_display = ('id','tid','tname','temail')


admin.site.register(Teacher,TeacherAdmin)
