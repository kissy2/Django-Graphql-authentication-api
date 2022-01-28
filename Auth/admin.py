from django.contrib import admin
from .models import ExtendUser
from django.apps import apps


admin.site.register(ExtendUser)
app = apps.get_app_config('graphql_auth')

for model in app.models.values():
    admin.site.register(model)