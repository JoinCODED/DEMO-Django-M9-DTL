from django.contrib import admin

from articles import models

to_register = [
    models.Author,
    models.Article,
]

admin.site.register(to_register)
