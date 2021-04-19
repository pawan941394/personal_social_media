from django.contrib import admin
from social.models import FollowUser, MYPost,MYProfile,PostComment,PostLike,contactinfo
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class FollowUserAdmin(ModelAdmin):
    list_display = ["profile","followed_by"]
    search_fields = ["profile","followed_by"]
    list_filter = ["profile","followed_by"]
admin.site.register(FollowUser,FollowUserAdmin)



class MYPostAdmin(ModelAdmin):
    list_display = ["subject","cr_date","uploaded_by"]
    search_fields = ["subject","msg","uploaded_by"]
    list_filter = ["uploaded_by","cr_date"]
admin.site.register(MYPost,MYPostAdmin)



class MYProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name","status","phone_no"]
    list_filter = ["gender","status"]
admin.site.register(MYProfile,MYProfileAdmin)



class PostCommentAdmin(ModelAdmin):
    list_display = ["post","msg"]
    search_fields = ["msg","post","commented_by"]
    list_filter = ["cr_date","flag"]
admin.site.register(PostComment,PostCommentAdmin)






class PostLikeAdmin(ModelAdmin):
    list_display = ["post","liked_by"]
    search_fields = ["post","liked_by"]
    list_filter = ["cr_date"]
admin.site.register(PostLike,PostLikeAdmin)


class contactinfoAdmin(ModelAdmin):
    list_display = ["Cname"]
admin.site.register(contactinfo,contactinfoAdmin)

