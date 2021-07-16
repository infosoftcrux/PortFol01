from django.contrib import admin
from .models import About,Experience,Social_links,Skills,Education,Projects,Contact,loginform

# Register your models here.
admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Social_links)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Contact)
admin.site.register(loginform)