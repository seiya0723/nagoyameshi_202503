from django.contrib import admin
from django.contrib import admin
from .models import Category,Restaurant,Review,Favorite,Reservation,PremiumUser
from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    list_display	= [ "id", "name", "created_at", "updated_at" ]

    search_fields = [ "name" ]

class RestaurantAdmin(admin.ModelAdmin):
    list_display	= [ "id", "category", "name", "image", "description", "start_at", "end_at", "cost", "post_code", "address", "tel", "created_at", "updated_at" ]

    search_fields = [ "name" ]
    list_filter = ["category"]

    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.image.url))

class ReviewAdmin(admin.ModelAdmin):
    list_display	= [ "id", "restaurant", "user", "content", "created_at", "updated_at" ]

class FavoriteAdmin(admin.ModelAdmin):
    list_display	= [ "id", "user", "restaurant", "created_at" ]

class ReservationAdmin(admin.ModelAdmin):
    list_display	= [ "id", "user", "restaurant", "datetime", "headcount", "created_at", "updated_at" ]

class PremiumUserAdmin(admin.ModelAdmin):
    list_display	= [ "id", "user", "premium_code" ]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Favorite,FavoriteAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(PremiumUser,PremiumUserAdmin)
