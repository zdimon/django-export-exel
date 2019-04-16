from django.db import models

class ShopCommodity(models.Model):
    commodity_id = models.AutoField(db_column='commodity_ID', primary_key=True)  # Field name made lowercase.
    dom_id = models.IntegerField()
    cod = models.CharField(max_length=100)
    commodity_price = models.FloatField()
    cur_id = models.IntegerField()
    commodity_old_price = models.FloatField()
    commodity_ves = models.FloatField()
    commodity_status = models.CharField(max_length=100)
    commodity_bigphoto = models.CharField(max_length=100)
    commodity_visible = models.CharField(max_length=100)
    commodity_add_date = models.CharField(max_length=20)
    commodity_action = models.IntegerField()
    commodity_hit = models.IntegerField()
    commodity_new = models.IntegerField()
    commodity_order = models.IntegerField()
    vendor = models.IntegerField()
    from_url = models.CharField(max_length=300)
    recomandate = models.CharField(max_length=200)
    lng_id = models.IntegerField()
    alias = models.CharField(max_length=200)
    use_alias = models.IntegerField()
    com_name = models.CharField(max_length=200)
    com_desc = models.TextField()
    com_fulldesc = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_commodity'



class ShopCategories(models.Model):
    categories_of_commodities_id = models.AutoField(primary_key=True)
    categories_of_commodities_photo = models.CharField(max_length=100)
    categories_of_commodities_parrent = models.IntegerField()
    categories_of_commodities_order = models.IntegerField()
    categories_of_commodities_add_date = models.CharField(max_length=19)
    lng_id = models.IntegerField()
    cat_name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    use_alias = models.IntegerField()
    cat_desc = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()
    h1 = models.CharField(max_length=200)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_categories'

class ShopCommoditiesCategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    commodityid = models.IntegerField(db_column='commodityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_commodities-categories'


class ShopCategoriesFilters(models.Model):
    filtr_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    filtr_order = models.IntegerField()
    fitr_catid = models.IntegerField()
    filtr_typeid = models.IntegerField()
    necessarily = models.IntegerField()
    list_parent = models.IntegerField()
    add_date = models.CharField(max_length=20)
    lng_id = models.IntegerField()
    filtr_name = models.CharField(max_length=200)
    filtr_desc = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'shop_categories-filters'