import xlwt
from django.http import HttpResponse

from .models import Order

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="applicants.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
    'customer', 'phone', 'Product', 'statur', 'note', 'order_content'
    ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    order = Order.objects.all()
    data = []
    count = 1
    for order in order:
        sl = count
        count += 1
        customer = order.customer.name
        customer_phone = order.customer.phone
        product = order.Product.name
        statur = order.statur
        note = order.note
        content = order.order_content
        single_data=(customer,customer_phone , product, statur, note, content)
        data.append(single_data)
    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
