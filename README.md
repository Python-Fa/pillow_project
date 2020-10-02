# 🔥پروژه پیلو
![N|Solid](https://github.com/ashkanjalaliQ/pillow_project/blob/master/image/pillow.png?raw=true)
این پروژه اپن سورس برای کار با عکس ها هست. با استفاده از این برنامه میتونید روی عکس هایتان انواع افکت هارو اعمال کنید
## لیست تغییرات
### 99/6/30
فایل اصلی برنامه با تغییراتی روبرو شده است.
چند قسمت جدید به برنامه اضافه کردم که کار باهاش رو راحت تر میکنه.
خوشحال میشم امتحانش کنید...

### 99/7/1
اضافه کردن فایل راهنما برای آشنا شدن بازدیدکنندگان با پروژه

### 99/7/5
قابلیت اجرا کردن برنامه با یک کامند مهیا شد.
یعنی فقط با یک خط میتونید همه درخواست هایتان نظیر بازکردن عکس، ویرایش عکس و سیو کردن عکس را انجام دهید.
قسمت جذاب برنامه اینجاست که اگر کلماتی مثل اسم افکت هارو اشتباه بنویسید، برنامه نزدیک ترین کلمه به اون کلمه اشتباه رو پیدا میکنه و جای اون میذاره

### 99/7/11
اضافه کردن چند افکت دیگر به برنامه.
اضافه کردن بخش هلپ به برنامه

## نصب لایبرری ها
```
pip install -r requirements.txt
```

## تابع های اعمال فیلتر
در ابتدا باید کتابخانه پیلو را فراخوانی کنید:
```python
from PIL import ImageOps, ImageChops
```
### Grayscale
```python
def gray_scale(image):
    image = ImageOps.grayscale(image)
    image = image.convert('RGB')
    return image
```
### Negative
```python
def negative(image):
    image = ImageChops.invert(image)
    image = image.convert('RGB')
    return image
```
### Black and White
```python
def b_and_w(image):
    gray = image.convert('L')
    image = gray.point(lambda x: 0 if x < 128 else 255, '1')
    image = image.convert('RGB')
    return image
```

## طریقه استفاده⚡
```python
python main.py
```
### اجرای برنامه با یک دستور
```
>>> Please Enter Command
"[-nr/-r] + {image address}" edit [grayscale/negative/blackandwhite] "{export name}"
```

### قابلیت تشخیص کلمه اشتباه
این قابلیت به شما کمک میکند که اگر نام افکتی را غلط نوشتید، برنامه نزدیک ترین کلمه به کلمه اشتباه شما را پیدا کند و جای آن بگذارد.

#### مثال
```
>>> Please Enter Command
"-r photo.png" edit grayscfel negitave balkandwite "Salam_aziz"
```
شکل تصحیح شده:
```
"-r photo.png" edit grayscale negative blackandwhite "Salam_aziz"
```
> در این صورت برنامه دستور شما به صورت شکل بالا تصحیح میکند

### طریقه استفاده از بخش هلپ
```
>>> Please Enter Command
--help
```

## لیست کار ها
- [x] ساخت افکت های جدید
- [x] ساخت قسمت help
- [ ] چک کردن کامند کاربر و پیشنهاد به او
- [x] ساخت افکت سفید و سیاه
- [x] ساخت افکت نگاتیو
- [x] ساخت افکت گری اسکیل
- [x] قابلیت دیدن پیشنمایش عکس قبل از ذخیره
- [x] نشان دادن تغییراتی که روی عکس اعمال کرده اید
- [x] اجرای برنامه فقط با یک خط دستور
- [x] قابلیت تشخیص کلمه اشتباه نظیر نام افکت و تصحیح آن
