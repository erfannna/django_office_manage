from jalali_date_new.utils import datetime2jalali
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
import io
from django.conf import settings
import arabic_reshaper
from bidi.algorithm import get_display


# PDF styling variables
TABLE_STYLE = TableStyle([
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("LEADING", (0, 0), (-1, -1), 20),
    ("FONTNAME", (0, 0), (-1, -1), "Vazirmatn"),  # استفاده از فونت فارسی
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),  # پس‌زمینه‌ی هدر
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # رنگ متن هدر
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # راست‌چین کردن متن
    ("VALIGN", (0, 0), (-1, -1), "TOP"),  # بالاچین کردن متن
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),  # فاصله پایین هدر
    ("TOPPADDING", (0, 0), (-1, 0), 10),  # فاصله بالا هدر
    ("GRID", (0, 0), (-1, -1), 1, colors.black),  # خطوط جدول
])

FONT_PATH = os.path.join(settings.STATIC_ROOT, "fonts/Vazirmatn-Regular.ttf")
pdfmetrics.registerFont(TTFont("Vazirmatn", FONT_PATH))

BOLD_FONT_PATH = os.path.join(settings.STATIC_ROOT, "fonts/Vazirmatn-Bold.ttf")
pdfmetrics.registerFont(TTFont("VazirmatnBold", BOLD_FONT_PATH))

P_STYLE = ParagraphStyle(name='Right',
                         alignment=TA_CENTER,
                         fontName='Vazirmatn',
                         fontSize=10)
T_STYLE = ParagraphStyle(name='Right',
                         alignment=TA_CENTER,
                         fontName='VazirmatnBold',
                         fontSize=18,
                         spaceAfter=30)

def fix_persian_text(text):
    """ Persian Chars Fix for ReportLab """
    if text is None:
        return ""
    reshaped_text = arabic_reshaper.reshape(text)  # اصلاح اتصال حروف
    return get_display(reshaped_text)  # تنظیم راست به چپ


def generate_buy_order_pdf(logs):
    buffer = io.BytesIO()

    # ایجاد PDF
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(A4))

    title = Paragraph(fix_persian_text("سوابق درخواست های خرید کالا"), T_STYLE)
    elements = [title]

    # **۱. ساخت هدر جدول**
    data = [["انجام شد", "وضعیت", "تاریخ", "توضیحات", "نوع", "تعداد", "برند", "نام کالا", "متقاضی", "شناسه"]]
    data = [[fix_persian_text(str(x)) for x in data[0]]]

    # **۲. اضافه کردن داده‌ها از دیتابیس**
    for log in logs:
        data.append([
            fix_persian_text(str("بله")) if log.completed else fix_persian_text(str("خیر")),
            fix_persian_text(str(log.status)),
            datetime2jalali(log.created).strftime("%Y/%m/%d - %H:%M"),
            Paragraph(fix_persian_text(str(log.description)) or "-", P_STYLE),
            fix_persian_text(str(log.order_type)),
            log.count,
            Paragraph(fix_persian_text(str(log.brand)), P_STYLE),
            Paragraph(fix_persian_text(str(log.name)), P_STYLE),
            Paragraph(fix_persian_text(str(log.user)), P_STYLE),
            log.id
        ])

    # **۳. ساخت جدول**
    table = Table(data, colWidths=[50, 70, 100, 150, 50, 50, 80, 100, 80, 50], style=TABLE_STYLE, repeatRows=1)

    # **۵. اضافه کردن جدول به PDF**
    elements.append(table)
    pdf.build(elements)

    buffer.seek(0)
    return buffer


def generate_stock_order_pdf(logs):
    buffer = io.BytesIO()

    # ایجاد PDF
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(A4))

    title = Paragraph(fix_persian_text("سوابق درخواست های کالا از انبار"), T_STYLE)
    elements = [title]

    # **۱. ساخت هدر جدول**
    data = [["انجام شد", "وضعیت", "تاریخ", "توضیحات", "نوع", "تعداد", "برند", "نام کالا", "متقاضی", "شناسه"]]
    data = [[fix_persian_text(str(x)) for x in data[0]]]

    # **۲. اضافه کردن داده‌ها از دیتابیس**
    for log in logs:
        data.append([
            fix_persian_text(str("بله")) if log.completed else fix_persian_text(str("خیر")),
            fix_persian_text(str(log.status)),
            datetime2jalali(log.created).strftime("%Y/%m/%d - %H:%M"),
            Paragraph(fix_persian_text(str(log.description)) or "-", P_STYLE),
            fix_persian_text(str(log.order_type)),
            log.count,
            Paragraph(fix_persian_text(str(log.brand)), P_STYLE),
            Paragraph(fix_persian_text(str(log.name)), P_STYLE),
            Paragraph(fix_persian_text(str(log.user)), P_STYLE),
            log.id
        ])

    # **۳. ساخت جدول**
    table = Table(data, colWidths=[50, 70, 100, 150, 50, 50, 80, 100, 80, 50], style=TABLE_STYLE, repeatRows=1)

    # **۵. اضافه کردن جدول به PDF**
    elements.append(table)
    pdf.build(elements)

    buffer.seek(0)
    return buffer


def generate_vacation_req_pdf(logs):
    buffer = io.BytesIO()

    # ایجاد PDF
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(A4))

    title = Paragraph(fix_persian_text("سوابق درخواست های مرخصی"), T_STYLE)
    elements = [title]


    # **۱. ساخت هدر جدول**
    headers = ["شناسه", "متقاضی", "جایگزین", "نوع", "شروع", "پایان", "مدت", "توضیحات", "ثبت", "وضعیت"]
    headers.reverse()
    reshaped_headers = [fix_persian_text(h) for h in headers]
    data = [reshaped_headers]

    # **۳. تبدیل داده‌ها به لیست و اصلاح فارسی**
    for log in logs:
        data.append([
            fix_persian_text(str(log.status)),
            datetime2jalali(log.created).strftime("%Y/%m/%d - %H:%M"),
            Paragraph(fix_persian_text(str(log.description)) or "-", P_STYLE),
            fix_persian_text(str(log.duration)),
            datetime2jalali(log.end_date).strftime("%Y/%m/%d - %H:%M"),
            datetime2jalali(log.start_date).strftime("%Y/%m/%d - %H:%M"),
            fix_persian_text(str(log.type)),
            Paragraph(fix_persian_text(str(log.alternative)), P_STYLE),
            Paragraph(fix_persian_text(str(log.user)), P_STYLE),
            log.id
        ])

    # **۳. ساخت جدول**
    table = Table(data, colWidths=[60, 100, 150, 40, 100, 100, 40, 80, 80, 50], style=TABLE_STYLE, repeatRows=1)

    # **۵. اضافه کردن جدول به PDF**
    elements.append(table)
    pdf.build(elements)

    buffer.seek(0)
    return buffer


def generate_problem_reps_pdf(logs):
    buffer = io.BytesIO()

    # ایجاد PDF
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(A4))

    title = Paragraph(fix_persian_text("سوابق خطاهای ثبت شده"), T_STYLE)
    elements = [title]

    # **۱. ساخت هدر جدول**
    data = [["موثر بوده/نبوده", "تاریخ", "توضیحات", "اقدامات پیشگیری", "اقدامات اصلاحی", "نوع خطا", "اعلام کننده", "شناسه"]]
    data = [[fix_persian_text(str(x)) for x in data[0]]]

    # **۲. اضافه کردن داده‌ها از دیتابیس**
    for log in logs:
        data.append([
            fix_persian_text(str("بله")) if log.effective else fix_persian_text(str("خیر")),
            datetime2jalali(log.created).strftime("%Y/%m/%d - %H:%M"),
            Paragraph(fix_persian_text(str(log.description)) or "-", P_STYLE),
            Paragraph(fix_persian_text(str(log.prevention_actions)) or "-", P_STYLE),
            Paragraph(fix_persian_text(str(log.corrective_actions)) or "-", P_STYLE),
            fix_persian_text(str(log.type)),
            Paragraph(fix_persian_text(str(log.user)), P_STYLE),
            log.id
        ])

    # **۳. ساخت جدول**
    table = Table(data, colWidths=[50, 100, 100, 100, 100, 80, 80, 50], style=TABLE_STYLE, repeatRows=1)

    # **۵. اضافه کردن جدول به PDF**
    elements.append(table)
    pdf.build(elements)

    buffer.seek(0)
    return buffer