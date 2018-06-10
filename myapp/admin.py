from django.contrib import admin
from .models import Profile,Post,Comment,like,dislike
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(like)
admin.site.register(dislike)