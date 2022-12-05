from django.contrib import admin

from .models import Category, Post


@admin.action(description='опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='убрать из публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    prepopulated_fields = {
        'slug': ('name', )
    }
    actions = (make_published, make_unpublished)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # actions_on_top = True
    # actions_on_bottom = True
    #
    # actions_selection_counter = True
    list_display = ('id', 'date', 'title', )
    readonly_fields = ('date_created', )
    ordering = ('is_published', '-date_created')
    list_display_links = ('id', )
    # list_editable = ('title', )
    list_filter = ('is_published', 'date_created', )
    # date_hierarchy = 'date_created'
    # exclude = ['date_created']      нельзя вместе с "fieldsets" - ошибка
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



