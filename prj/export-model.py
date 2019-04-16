# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseCities(models.Model):
    city_id = models.AutoField(primary_key=True)
    region_id = models.PositiveIntegerField()
    country_id = models.PositiveIntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_cities'


class BaseCitiesDescriptions(models.Model):
    city_id = models.PositiveIntegerField()
    lng_id = models.IntegerField()
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'base_cities-descriptions'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    item_prefix = models.CharField(max_length=10)
    item_id = models.IntegerField()
    parent_id = models.IntegerField()
    comment_date = models.CharField(max_length=20)
    comment_email = models.CharField(max_length=100)
    comment_tel = models.CharField(max_length=100)
    comment_ip = models.CharField(max_length=15)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    comment_text = models.TextField()
    comment_plus = models.TextField()
    comment_minus = models.TextField()
    comment_rat = models.IntegerField()
    visible = models.IntegerField()
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'comments'


class ContentArticles(models.Model):
    articleid = models.AutoField(db_column='articleID', primary_key=True)  # Field name made lowercase.
    dom_id = models.IntegerField()
    lng_id = models.IntegerField()
    name = models.CharField(max_length=300)
    h1 = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    description = models.TextField()
    keywords = models.TextField()
    content = models.TextField()
    alias = models.CharField(max_length=100)
    use_alias = models.IntegerField()
    text = models.TextField()
    add_date = models.CharField(max_length=20)
    order = models.IntegerField()
    image = models.IntegerField()
    parent = models.IntegerField()
    visible = models.IntegerField()
    menu = models.IntegerField()
    block = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_articles'


class ContentFieldsValues(models.Model):
    val_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField()
    field_id = models.IntegerField()
    value1 = models.CharField(max_length=200)
    value2 = models.TextField()
    value3 = models.FloatField()
    value4 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'content_fields_values'


class ContentImages(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_artid = models.IntegerField()
    order = models.IntegerField()
    img_name = models.CharField(max_length=200)
    img_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'content_images'


class ContentTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_types'


class ContentTypesFields(models.Model):
    fileld_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=200)
    field_kind = models.IntegerField()
    field_typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_types_fields'


class Counter(models.Model):
    domenid = models.IntegerField(db_column='domenID')  # Field name made lowercase.
    full_url = models.CharField(max_length=1000)
    date = models.DateField()
    atime = models.TimeField()
    ip = models.CharField(max_length=100)
    brouser = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    referrer = models.CharField(max_length=300)
    query_word = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'counter'


class CounterArhive(models.Model):
    domenid = models.IntegerField(db_column='domenID')  # Field name made lowercase.
    date = models.DateField()
    hits = models.IntegerField()
    users = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'counter_arhive'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domens(models.Model):
    domenid = models.AutoField(db_column='domenID')  # Field name made lowercase.
    domen = models.CharField(max_length=100)
    www_domen = models.CharField(max_length=100)
    lng_id = models.IntegerField()
    cur_id = models.IntegerField()
    theme_name = models.CharField(max_length=50)
    urlend = models.CharField(max_length=10)
    watermark = models.IntegerField()
    comitemst = models.IntegerField()
    comitemsx = models.IntegerField()
    comitemsy = models.IntegerField()
    catitemscount = models.IntegerField()
    catitemsx = models.IntegerField()
    catitemsy = models.IntegerField()
    catitemst = models.IntegerField()
    addcomimgx = models.IntegerField()
    addcomimgy = models.IntegerField()
    addcomimgt = models.IntegerField()
    artimgx = models.IntegerField()
    artimgy = models.IntegerField()
    artimgt = models.IntegerField()
    artimgaddx = models.IntegerField()
    artimgaddy = models.IntegerField()
    artimgaddt = models.IntegerField()
    email = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'domens'


class DomensDescription(models.Model):
    dom_id = models.IntegerField(unique=True)
    lng_id = models.IntegerField()
    title = models.CharField(max_length=200)
    keywords = models.TextField()
    description = models.TextField()
    content = models.TextField()
    main_page_title = models.TextField()
    main_page_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'domens_description'


class Languages(models.Model):
    languages_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=2)
    image = models.CharField(max_length=64, blank=True, null=True)
    directory = models.CharField(max_length=32, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'languages'


class LanguagesTranslate(models.Model):
    word_id = models.IntegerField()
    lng_id = models.IntegerField()
    word_translate = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'languages_translate'


class LanguagesWords(models.Model):
    word_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    word_sys_word = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'languages_words'


class Links(models.Model):
    link_id = models.AutoField(primary_key=True)
    link_name = models.CharField(max_length=200)
    lng_id = models.IntegerField()
    domenid = models.IntegerField(db_column='domenID')  # Field name made lowercase.
    text = models.TextField()
    area = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'links'


class LinksAreas(models.Model):
    area_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    area_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'links_areas'


class LinksTypes(models.Model):
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'links_types'


class Modules(models.Model):
    module_id = models.AutoField()
    module_order = models.IntegerField()
    module_name = models.CharField(max_length=100)
    module_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'modules'


class Parser(models.Model):
    name = models.CharField(max_length=200)
    cat_id = models.CharField(max_length=200)
    h1 = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    price2 = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    cod = models.CharField(max_length=200)
    dopimg = models.CharField(max_length=200)
    links11 = models.TextField()
    per = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    from_field = models.CharField(db_column='from', max_length=200)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'parser'


class SeoLinks(models.Model):
    dom_id = models.IntegerField()
    from_field = models.CharField(db_column='from', max_length=300)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'seo_links'


class SeoPages(models.Model):
    dom_id = models.IntegerField()
    url = models.CharField(max_length=300)
    lvl = models.IntegerField()
    type = models.IntegerField()
    in_field = models.IntegerField(db_column='in')  # Field renamed because it was a Python reserved word.
    out = models.IntegerField()
    weight1 = models.FloatField()
    weight2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'seo_pages'


class SeoStock(models.Model):
    id = models.IntegerField()
    dom_id = models.IntegerField()
    url = models.CharField(max_length=300)
    lvl = models.IntegerField()
    use = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seo_stock'


class ShopCategories(models.Model):
    categories_of_commodities_id = models.AutoField(db_column='categories_of_commodities_ID')  # Field name made lowercase.
    dom_id = models.IntegerField()
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


class ShopCategoriesFilters(models.Model):
    filtr_id = models.AutoField()
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


class ShopCommoditiesCategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    commodityid = models.IntegerField(db_column='commodityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_commodities-categories'


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


class ShopCur(models.Model):
    cur_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    cur_name = models.CharField(max_length=100)
    cur_val = models.FloatField()
    full_name = models.CharField(max_length=100)
    cur_show = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shop_cur'


class ShopDelivery(models.Model):
    dom_id = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    free = models.FloatField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_delivery'


class ShopDiscount(models.Model):
    dis_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    dis_val1 = models.FloatField()
    dis_val2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_discount'


class ShopDiscount2(models.Model):
    dis_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    dis_val1 = models.FloatField()
    dis_val2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_discount2'


class ShopFiltersLists(models.Model):
    list_order = models.IntegerField()
    list_filterid = models.IntegerField()
    lng_id = models.IntegerField()
    list_name = models.CharField(max_length=200)
    list_parentid = models.IntegerField()
    list_parentfiltrid = models.IntegerField()
    list_id = models.IntegerField()
    add_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'shop_filters-lists'


class ShopFiltersValues(models.Model):
    ticket_id = models.IntegerField()
    ticket_filterid = models.IntegerField()
    ticket_value = models.TextField()
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_filters-values'


class ShopImages(models.Model):
    img_id = models.AutoField()
    com_id = models.IntegerField()
    order = models.IntegerField()
    img_name = models.CharField(max_length=200)
    img_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_images'


class ShopOrders(models.Model):
    status = models.IntegerField()
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    user_comments = models.TextField()
    labels = models.IntegerField()
    user_id = models.IntegerField()
    comments = models.TextField()
    discount = models.FloatField()
    delivery = models.IntegerField()
    delivery_price = models.FloatField()
    cur_id = models.IntegerField()
    payment = models.IntegerField()
    cod = models.CharField(max_length=100)
    commission = models.FloatField()
    dom_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_orders'


class ShopOrdersComs(models.Model):
    offer_id = models.IntegerField()
    com_id = models.IntegerField()
    cur_id = models.IntegerField()
    count = models.IntegerField()
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_orders_coms'


class ShopPaymentsMethods(models.Model):
    dom_id = models.IntegerField()
    name = models.CharField(max_length=200)
    commision = models.FloatField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_payments_methods'


class ShopRecommendation(models.Model):
    rec_id = models.AutoField(primary_key=True)
    rec_com_id = models.IntegerField()
    rec_other_com_id = models.IntegerField()
    rec_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_recommendation'


class Sliders(models.Model):
    slider_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    slider_name = models.CharField(max_length=200)
    slider_x = models.IntegerField()
    slider_y = models.IntegerField()
    slider_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sliders'


class SlidersImg(models.Model):
    sliderimg_id = models.AutoField(primary_key=True)
    sliderimg_name = models.CharField(max_length=200)
    sliderimg_desc = models.TextField()
    sliderimg_order = models.IntegerField()
    sliderimg_lngid = models.IntegerField()
    sliderimg_sliderid = models.IntegerField()
    add_date = models.CharField(max_length=20)
    url = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sliders_img'


class SystemLongload(models.Model):
    long_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    long_date = models.CharField(max_length=20)
    long_url = models.CharField(max_length=300)
    long_time = models.FloatField()
    long_time2 = models.FloatField()
    long_ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'system_longload'


class SystemSessions(models.Model):
    session_id = models.CharField(unique=True, max_length=255)
    dom_id = models.IntegerField()
    date_touched = models.DateTimeField()
    sess_data = models.TextField()
    user_ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'system_sessions'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    dom_id = models.IntegerField()
    user_name = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=32)
    user_realpassword = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_image = models.CharField(max_length=200)
    user_admin = models.PositiveIntegerField()
    user_realname = models.CharField(max_length=200)
    user_tel = models.CharField(max_length=100)
    user_birthday = models.DateField()
    user_sex = models.IntegerField()
    user_work = models.TextField()
    user_country = models.CharField(max_length=100)
    user_region = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)
    user_adr = models.CharField(max_length=100)
    user_last_been = models.CharField(max_length=100)
    user_registred_date = models.CharField(max_length=100)
    user_registred_code = models.CharField(max_length=100)
    user_managerid = models.IntegerField()
    user_discount = models.IntegerField()
    user_soc_provider = models.CharField(max_length=100)
    user_soc_page = models.CharField(max_length=300)
    user_soc_id = models.CharField(max_length=200)
    user_soc_pass = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'users'
