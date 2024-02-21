from django.contrib import admin
from .models import Funfacts
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Funfacts)
class FunfactsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
