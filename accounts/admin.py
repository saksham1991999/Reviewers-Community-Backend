from django.contrib import admin
import nested_admin

from .models import User


class UserAdmin(nested_admin.NestedModelAdmin):
    list_display = (
        'username',
        'first_name',
        'email',
        'city',
    )


admin.site.site_header = 'Reviewers Community'
admin.site.register(User, UserAdmin)