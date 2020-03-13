from django.contrib import admin
from status.models import Status as StatusModel
from .forms import StatusForm


@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','user', '__str__',  'img']
    form = StatusForm


# admin.site.register(StatusModel, StatusAdmin)  # TODO