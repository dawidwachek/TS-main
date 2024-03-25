from django.contrib import admin
from .models import Coupon, Reflink, Banner, Voucher


@admin.register(Reflink)
class ReflinkAdmin(admin.ModelAdmin):
    list_display = ['reflink_id', 'name_user', 'uses_reflink']
    readonly_fields = ["reflink_id","created_at", 'uses_reflink', 'link_reflink']
    list_filter = ['name_user']
    search_fields = ['name_user', 'reflink_id']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_id', 'coupon_name','is_active','uses_coupon', 'type_coupon','max_value_coupon','value_coupon', 'max_uses_coupon', 'zero_amount', "assigment"]
    readonly_fields = ["coupon_id","created_at",'uses_coupon']
    list_filter = ['type_coupon','zero_amount','is_active', 'assigment']
    search_fields = ['coupon_id', 'coupon_name']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner_id','is_active', 'has_link']
    readonly_fields = ['banner_id', 'created_at']
    search_fields = ['text']
    list_filter = ['is_active', 'has_link']

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'is_active', 'for_user','user']
    readonly_fields = ['is_used']
    search_dields = ['id', 'slug']
    list_filter = ['is_active']