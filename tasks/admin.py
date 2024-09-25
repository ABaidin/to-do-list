from django.contrib import admin
from django.contrib.auth.models import Group, User

from tasks.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content", )
    list_filter = ("tags", "is_done")


admin.site.register(Tag)

admin.site.unregister(Group)
admin.site.unregister(User)
