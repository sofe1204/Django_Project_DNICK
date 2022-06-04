from django.contrib import admin
from BlogPost.models import user, BlogPost, Commentar
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

class userAdmin(admin.ModelAdmin):
    # pass
    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(user, userAdmin)

class CommentarAdmin(admin.StackedInline):
    model = Commentar
    extra = 0

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

#admin.site.register(Commentar,CommentarAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = (("date_create", DateTimeRangeFilter),)
    search_fields = ("title", "content")
    inlines = [CommentarAdmin,]
    exclude = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        #Block.objects.add_block(request.user, obj.user)
        return True

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     if request.POST.get('action') == 'delete_selected':
    #         messages.add_message(request,messages.ERROR(
    #             "Are you sure you want to delete this Post?"
    #         ))
    #     return True

admin.site.register(BlogPost, BlogPostAdmin)


class BlogPostCommentarAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True
# admin.site.register(BlogPostCommentar, BlogPostCommentarAdmin)
