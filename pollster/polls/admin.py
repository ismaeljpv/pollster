from django.contrib import admin

from .models import Question, Choice

admin.AdminSite.site_header = 'Pollster Admin'
admin.AdminSite.site_title = 'Pollster Admin Area'
admin.AdminSite.index_title = 'Welcome to the Pollster Admin Area'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('question_text',), }),
        ('Date Information', {'fields': ('publish_date',), 'classes': ('collapse',), }),
    )
    inlines = [ChoiceInline]
    

#admin.site.register(Question)  normal form
#admin.site.register(Choice)    normal form

admin.site.register(Question, QuestionAdmin)
