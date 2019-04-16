from django.core.management.base import BaseCommand, CommandError

from main.models import ShopCommodity, ShopCategories, ShopCommoditiesCategories, ShopCategoriesFilters
import xlwt


def export_catalog(sheet):
    sheet.write(0, 0, 'Номер_группы')
    sheet.write(0, 1, 'Название_группы')
    sheet.write(0, 2, 'Идентификатор_группы')
    sheet.write(0, 3, 'Номер_родителя')
    sheet.write(0, 4, 'Идентификатор_родителя')
    x = 1
    for cat in ShopCategories.objects.all():
        sheet.write(x, 0, cat.categories_of_commodities_id)
        sheet.write(x, 1, cat.cat_name)
        sheet.write(x, 2, cat.categories_of_commodities_id)
        sheet.write(x, 3, cat.categories_of_commodities_parrent)
        x += 1
    return sheet

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Export data')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Export Products Sheet')
        cats = wb.add_sheet('Export Groups Sheet')
        export_catalog(cats)
        # title


        ws.write(0, 0, 'Код_товара')
        ws.write(0, 1, 'Название_позиции')
        ws.write(0, 2, 'Описание')
        ws.write(0, 3, 'Тип_товара')
        ws.write(0, 4, 'Цена')
        ws.write(0, 5, 'Валюта')
        ws.write(0, 6, 'Единица_измерения')
        ws.write(0, 7, 'Ссылка_изображения')
        ws.write(0, 8, 'Наличие')
        ws.write(0, 9, 'Номер_группы')
        ws.write(0, 10, 'Название_группы')
        ws.write(0, 11, 'Уникальный_идентификатор')
        ws.write(0, 12, 'Производитель')
        ws.write(0, 13, 'Страна_производитель')

        cnt = 14
        for parameter in ShopCategoriesFilters.objects.all():
            ws.write(0, cnt, 'Название_Характеристики')
            ws.write(0, cnt+1, 'Измерение_Характеристики')
            ws.write(0, cnt+2, 'Значение_Характеристики')
            cnt += 3
        

        x = 1
        for item in ShopCommodity.objects.all()[:10]:
            ws.write(x, 0, item.commodity_id)
            ws.write(x, 1, item.com_name)
            ws.write(x, 2, item.com_fulldesc[:32000])
            ws.write(x, 3, 'r')
            ws.write(x, 4, item.commodity_price)
            ws.write(x, 5, 'UAH')
            ws.write(x, 6, 'шт.')
            img_url = 'http://www.climainvest.com.ua/%sstitle/%s.jpg' % (item.commodity_id, item.alias)
            ws.write(x, 7, img_url)
            ws.write(x, 8, '!')
            ws.write(x, 11, item.commodity_id)

            # category
            # select category for item
            try:
                i2c = ShopCommoditiesCategories.objects.get(commodityid=item.commodity_id)
                # select category
                cat = ShopCategories.objects.get(categories_of_commodities_id=i2c.categoryid)
                ws.write(x, 9, cat.categories_of_commodities_id)
                ws.write(x, 10, cat.cat_name)
            except:
                print('No category')

            # save parameters
            #cnt = 14
            #for parameter in ShopCategoriesFilters.objects.all():
            #    ws.write(x, cnt, parameter.filtr_name)
            #    ws.write(x, cnt+1, '')
            #    ws.write(x, cnt+2, 'Значение_Характеристики')
            #    cnt += 3

            #ws.write(x, 9, cat.cat_name)

            print(item.com_name)
            x += 1

        wb.save('export.xls')