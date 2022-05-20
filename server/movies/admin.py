from django.contrib import admin
from .models import Movie, Staff, Grade, Keyword


admin.site.register(Movie)
admin.site.register(Staff)
admin.site.register(Grade)
admin.site.register(Keyword)