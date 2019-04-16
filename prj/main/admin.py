from django.contrib import admin

# Register your models here.

from .models import ShopCommodity, ShopCategories

class ShopCommodityAdmin(admin.ModelAdmin):
    list_display = [
        'commodity_id', 
        'dom_id',
        'cod',
        'commodity_price',
        'cur_id',
        'commodity_old_price',
        'commodity_ves',
        'commodity_status',
        'commodity_bigphoto',
        'commodity_visible',
        'commodity_add_date',
        'commodity_action',
        'commodity_hit',
        'commodity_new',
        'commodity_order',
        'vendor',
        'from_url',
        'recomandate',
        'lng_id',
        'alias',
        'use_alias',
        'com_name',
        'com_desc',
        'com_fulldesc',
        'title',
        'description',
        'keywords',
        'weight',
        'height',
        'width',
        'depth'
        ]
    
admin.site.register(ShopCommodity, ShopCommodityAdmin)



class ShopCategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'cat_name', 
        'categories_of_commodities_parrent'
        ]
    
admin.site.register(ShopCategories, ShopCategoriesAdmin)

