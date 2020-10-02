<h1 dir="rtl">🔥پروژه پیلو</h1>
<p align="center">
  <img src="https://github.com/ashkanjalaliQ/pillow_project/blob/master/image/pillow.png?raw=true"/>
</p>
<p dir="rtl">این پروژه اپن سورس برای کار با عکس ها هست. با استفاده از این برنامه میتونید روی عکس هایتان انواع افکت هارو اعمال کنید</p>
<h2 dir="rtl">لیست تغییرات</h2>
<h3 dir="rtl">99/6/30</h3>
<p dir="rtl">
فایل اصلی برنامه با تغییراتی روبرو شده است.
چند قسمت جدید به برنامه اضافه کردم که کار باهاش رو راحت تر میکنه.
خوشحال میشم امتحانش کنید...
</p>
<h3 dir="rtl">99/7/1</h3>
<p dir="rtl">
اضافه کردن فایل راهنما برای آشنا شدن بازدیدکنندگان با پروژه
</p>
<h3 dir="rtl">99/7/5</h3>
<p dir="rtl">
قابلیت اجرا کردن برنامه با یک کامند مهیا شد.
یعنی فقط با یک خط میتونید همه درخواست هایتان نظیر بازکردن عکس، ویرایش عکس و سیو کردن عکس را انجام دهید.
قسمت جذاب برنامه اینجاست که اگر کلماتی مثل اسم افکت هارو اشتباه بنویسید، برنامه نزدیک ترین کلمه به اون کلمه اشتباه رو پیدا میکنه و جای اون میذاره
</p>
<h3 dir="rtl">99/7/11</h3>
<p dir="rtl">
اضافه کردن چند افکت دیگر به برنامه.
اضافه کردن بخش help به برنامه
</p>
<h2 dir="rtl">نصب لایبرری ها</h2>
<pre>
pip install -r requirements.txt
</pre>

<h2 dir="rtl">تابع های اعمال فیلتر</h2>
<p dir="rtl">
در ابتدا باید کتابخانه پیلو را فراخوانی کنید:
</p>
<pre lang="python">from PIL import ImageOps, ImageChops</pre>

<h3 dir="rtl">Grayscale</h3>
<pre lang="python">
def gray_scale(image):
    image = ImageOps.grayscale(image)
    image = image.convert('RGB')
    return image
</pre>
<h3 dir="rtl">Negative</h3>
<pre lang="python">
def negative(image):
    image = ImageChops.invert(image)
    image = image.convert('RGB')
    return image
</pre>
<h3 dir="rtl">Black and White<h3>
<pre lang="python">
def b_and_w(image):
    gray = image.convert('L')
    image = gray.point(lambda x: 0 if x < 128 else 255, '1')
    image = image.convert('RGB')
    return image
</pre>

<h2 dir="rtl">طریقه استفاده⚡</h2>
<pre lang="python">
python main.py
</pre>
<h3 dir="rtl">اجرای برنامه با یک دستور</h3>
<pre lang="python">
>>> Please Enter Command
"[-nr/-r] + {image address}" edit [grayscale/negative/blackandwhite] "{export name}"
</pre>

<h3 dir="rtl">قابلیت تشخیص کلمه اشتباه</h3>
<p dir="rtl">
این قابلیت به شما کمک میکند که اگر نام افکتی را غلط نوشتید، برنامه نزدیک ترین کلمه به کلمه اشتباه شما را پیدا کند و جای آن بگذارد.
</p>
<h4 dir="rtl">مثال</h4>
<pre lang="python">
>>> Please Enter Command
"-r photo.png" edit grayscfel negitave balkandwite "Salam_aziz"
</pre>
<p dir="rtl">
شکل تصحیح شده:
</p>
<pre lang="python">
"-r photo.png" edit grayscale negative blackandwhite "Salam_aziz"
</pre>
<p dir="rtl">
> در این صورت برنامه دستور شما به صورت شکل بالا تصحیح میکند
</p>
<h3 dir="rtl">طریقه استفاده از بخش help</h3>
<pre lang="python">
>>> Please Enter Command
--help
</pre>

<h2 dir="rtl">لیست کار ها</h2>

- [x] ساخت افکت های جدید
- [x] ساخت قسمت help
- [ ] چک کردن کامند کاربر و پیشنهاد به او
- [x] ساخت افکت سفید و سیاه
- [x] ساخت افکت نگاتیو
- [x] ساخت افکت گری اسکیل
- [x] قابلیت دیدن پیشنمایش عکس قبل از ذخیره
- [x] نشان دادن تغییراتی که روی عکس اعمال کرده اید
- [x] اجرای برنامه فقط با یک خط دستور
- [x]  قابلیت تشخیص کلمه اشتباه نظیر نام افکت و تصحیح آن
