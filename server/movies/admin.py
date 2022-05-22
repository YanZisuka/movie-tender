from django.contrib import admin
from .models import Movie, Staff, Rating, Keyword


admin.site.register(Movie)
admin.site.register(Staff)
admin.site.register(Rating)
admin.site.register(Keyword)