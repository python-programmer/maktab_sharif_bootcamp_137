import requests
import os


def download_file(url, filename=None):
    """
    یک فایل از URL دانلود کرده و در فایل محلی ذخیره می‌کند

    Args:
        url: آدرس اینترنتی فایل برای دانلود
        filename: نام فایل برای ذخیره‌سازی (اختیاری)
    """

    # اگر نام فایل مشخص نشده، از URL استخراج می‌کند
    if filename is None:
        filename = url.split('/')[-1]

    # درخواست GET برای دانلود فایل
    response = requests.get(url, stream=True)

    # بررسی موفقیت آمیز بودن درخواست
    if response.status_code == 200:
        # محاسبه حجم فایل
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        # باز کردن فایل برای نوشتن
        with open(filename, 'wb') as file:
            # دانلود فایل به صورت قطعه قطعه
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)

                    # نمایش پیشرفت دانلود
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        print(f"\rدر حال دانلود: {progress:.1f}% کامل", end='')

        print(f"\nدانلود کامل شد: {filename}")
        return True
    else:
        print(f"خطا در دانلود: کد وضعیت {response.status_code}")
        return False


# مثال استفاده
if __name__ == "__main__":
    # آدرس فایل برای دانلود
    file_url = "https://irsv.upmusics.com/dlw/Alireza%20Ghorbani%20%E2%80%93%20Bichare%20Del%20(320).mp3"

    # دانلود فایل
    download_file(file_url, "bichare-del.mp3")