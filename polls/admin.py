from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3


class PollAdmin(admin.ModelAdmin):
    #fields=['pub_date','question']
    fieldsets = [
            (None,            {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date']}),
         ]

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
