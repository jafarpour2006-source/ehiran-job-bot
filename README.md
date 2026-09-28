# ربات رصد استخدام بهداشت محیط ایران

نسخه v1.1 برای اجرای خودکار با GitHub Actions.

## عملکرد
- هر ۳ ساعت یک‌بار جستجوی وب
- جستجوی چندین کلیدواژه مرتبط با بهداشت محیط
- حذف آگهی‌های تکراری با SQLite
- ارسال موارد جدید به کانال تلگرام
- بدون اتصال به سایت

## راه‌اندازی سریع با GitHub
1. این پوشه را داخل یک Repository در GitHub قرار دهید.
2. در Repository Settings → Secrets and variables → Actions، این سه Secret را بسازید:
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHANNEL_ID = @behdashtmohitiran
   - SERPER_API_KEY
3. از Actions، workflow با نام EH Iran Jobs Scanner را باز کنید.
4. Run workflow را یک بار دستی اجرا کنید.
5. پس از آن طبق برنامه هر ۳ ساعت اجرا می‌شود.

توکن تلگرام و کلید API را هرگز در فایل‌های عمومی قرار ندهید.
