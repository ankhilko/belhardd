from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    prepopulated_fields = {
        'slug': ('name', )
    }


    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # actions_on_top = True
    # actions_on_bottom = True
    #
    # actions_selection_counter = True
    list_display = ('id', 'date', 'title', )
    ordering = ('is_published', '-date_created')
    list_display_links = ('id', )
    # list_editable = ('title', )
    list_filter = ('is_published', 'date_created', )
    # date_hierarchy = 'date_created'
    # exclude = ['date_created']      нельзя вместе с полями - ошибка
    fieldsets = (
        (
            'Основное',
            {
                'fields': ['title', 'descr'],
                'description': 'Осноные значения'
            }
        ),
        (
            'Дополнительное',
            {
                'fields': ['is_published', 'slug', 'category', 'author']
            }
        )
    )
    prepopulated_fields = {
        'slug': ('title', )
    }



# admin.site.register(Category)
# admin.site.register(Post)

# Register your models here.
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)



