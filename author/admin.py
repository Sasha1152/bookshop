from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'biography',
                    'image',
                    )

admin.site.register(Author, AuthorAdmin)
