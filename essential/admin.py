from django.contrib import admin

from essential.models import User, UserWithTask,Task,Project

# Register your models here.
admin.site.register(User)
admin.site.register(UserWithTask)
admin.site.register(Project)
admin.site.register(Task)