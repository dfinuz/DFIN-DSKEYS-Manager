# DFIN DSKEYS Manager

**DFIN DSKEYS Manager** Windows kompyuteridagi elektron raqamli imzo kalitlarini boshqarish uchun yaratilgan dasturdir. Dastur `DSKEYS` papkasidagi kalitlarni E-IMZO orqali tekshiradi, amal qilish muddatini ko‘rsatadi, muddati tugagan kalitlarni ajratadi va takroriy kalitlarni topadi.

> **Muhim:** dasturdan foydalanishdan oldin kompyuterga **Python 3.13 yoki undan yangi versiya** hamda **E-IMZO** o‘rnatilgan bo‘lishi kerak.

## Asosiy imkoniyatlar

- E-IMZO orqali sertifikatlar ro‘yxatini olish
- Kalitlarni amal qilish holati bo‘yicha guruhlash
- Ishlayotgan kalitlarni alohida ko‘rsatish
- 30 kun ichida muddati tugaydigan kalitlarni ko‘rsatish
- Muddati tugagan kalitlarni alohida ko‘rsatish
- Takroriy kalitlarni aniqlash
- Fayli topilmagan sertifikatlarni ko‘rsatish
- Muddati aniqlanmagan sertifikatlarni alohida ko‘rsatish
- Muddati tugagan kalitlarni boshqa papkaga ko‘chirish
- Tanlangan kalitlarni Windows savatiga yuborish
- Sichqonchaning o‘ng tugmasi orqali kalitni olib tashlash
- Ingliz va rus tillarida ishlash


## Tizim talablari

Dasturdan foydalanish uchun quyidagilar kerak:

- Windows 10 yoki Windows 11, 64 bit
- Python 3.13 yoki undan yangi versiya
- E-IMZO dasturi
- E-IMZO ishga tushirilgan holatda bo‘lishi
- ERI kalitlari saqlangan `C:\DSKEYS` papkasi
- Dastur va kalitlar bilan ishlash uchun yetarli foydalanuvchi ruxsati

## 1. Python o‘rnatish

### 1.1. Python yuklab olish

1. Brauzerda quyidagi manzilni oching:

   `https://www.python.org/downloads/windows/`

2. Python 3.13 yoki undan yangi versiyaning Windows uchun 64 bit o‘rnatuvchisini yuklab oling.
3. Yuklangan o‘rnatuvchi faylni ishga tushiring.

### 1.2. Python o‘rnatish vaqtida kerakli sozlama

Python o‘rnatish oynasida quyidagi belgi qo‘yilgan bo‘lishi shart:

```text
Add Python to PATH
```

Shundan keyin:

1. `Install Now` tugmasini bosing.
2. O‘rnatish yakunlanishini kuting.
3. O‘rnatish tugagach, kompyuterni qayta ishga tushirish tavsiya etiladi.

### 1.3. Python o‘rnatilganini tekshirish

1. `Win + R` tugmalarini bosing.
2. `cmd` deb yozing.
3. `Enter` tugmasini bosing.
4. Quyidagi buyruqni kiriting:

```bat
python --version
```

Yoki:

```bat
py --version
```

Natija taxminan quyidagicha bo‘lishi kerak:

```text
Python 3.13.x
```

Agar Python versiyasi ko‘rsatilsa, Python muvaffaqiyatli o‘rnatilgan.

## 2. Kerakli Python kutubxonasini o‘rnatish

Buyruqlar oynasida quyidagi buyruqni bajaring:

```bat
py -m pip install --upgrade send2trash
```

Agar `py` buyrug‘i ishlamasa, quyidagini bajaring:

```bat
python -m pip install --upgrade send2trash
```

`send2trash` kutubxonasi o‘chirilayotgan kalitlarni butunlay yo‘q qilish o‘rniga Windows savatiga yuborish uchun ishlatiladi.

> Dastur sertifikatlarning amal qilish muddatini E-IMZO orqali oladi. Oddiy tekshirish uchun PFX paroli talab qilinmaydi.

## 3. E-IMZO o‘rnatish

1. E-IMZO rasmiy o‘rnatuvchisini yuklab oling.
2. O‘rnatuvchi fayl ustiga sichqonchaning o‘ng tugmasini bosing.
3. `Administrator sifatida ishga tushirish` bandini tanlang.
4. O‘rnatish jarayonini yakunlang.
5. Kompyuterni qayta ishga tushiring.
6. E-IMZO dasturini ishga tushiring.

E-IMZO Windows tizim panelida ishlab turgan bo‘lishi kerak. DFIN DSKEYS Manager sertifikat ma’lumotlarini mahalliy E-IMZO xizmatidan oladi.

## 4. ERI kalitlarini tayyorlash

Odatda kalitlar quyidagi papkada saqlanadi:

```text
C:\DSKEYS
```

Kalit fayllari va papkalari ushbu joyda mavjudligini tekshiring.

Misol:

```text
C:\DSKEYS\kalit_nomi
```

Agar kalitlar boshqa papkada saqlangan bo‘lsa, dastur ichidagi `Browse` yoki `Обзор` tugmasi orqali kerakli papkani tanlash mumkin.

## 5. Dastur o‘rnatish

1. `DFIN_DSKEYS_Manager_Setup.exe` faylini ishga tushiring.
2. Windows xavfsizlik oynasi chiqsa, fayl manbasini tekshiring.
3. `Install` tugmasini bosing.
4. O‘rnatish yakunlanishini kuting.
5. Dasturga ish stoli yoki Start menyusi orqali kiring.

## 6. Dasturdan foydalanish

### 6.1. Tilni tanlash

Dastur oynasining yuqori qismidagi til ro‘yxatidan quyidagilardan birini tanlang:

- `English`
- `Русский`

Tanlangan til avtomatik saqlanadi va keyingi ishga tushirishda ham qo‘llanadi.

### 6.2. DSKEYS papkasini tanlash

Standart papka:

```text
C:\DSKEYS
```

Agar kerak bo‘lsa:

1. `Browse` yoki `Обзор` tugmasini bosing.
2. Kalitlar saqlangan papkani tanlang.
3. Papka tanlanganini tasdiqlang.

### 6.3. Kalitlarni tekshirish

1. E-IMZO ishlab turganini tekshiring.
2. `Scan E-IMZO` yoki `Сканировать E-IMZO` tugmasini bosing.
3. Dastur E-IMZO orqali sertifikat ma’lumotlarini oladi.
4. Tekshirish yakunlangach, kalitlar tegishli bo‘limlarda ko‘rinadi.

## 7. Dastur bo‘limlari

### Working yoki Действующие

Amal qilish muddati tugamagan va 30 kundan ko‘proq vaqt qolgan kalitlar.

### Expiring within 30 days yoki Истекают в течение 30 дней

Amal qilish muddati 30 kun ichida tugaydigan kalitlar.

Bunday kalitlarni oldindan yangilash tavsiya etiladi.

### Expired yoki Просроченные

Amal qilish muddati tugagan kalitlar.

Bu kalitlar odatda davlat portallariga kirish yoki hujjatlarni imzolash uchun ishlamaydi.

### Duplicates yoki Дубликаты

Bir xil sertifikat seriya raqamiga ega bo‘lgan takroriy kalitlar.

Takroriy kalitlarni o‘chirishdan oldin fayl nomi, joylashuvi va amal qilish muddatini diqqat bilan tekshiring.

### File not matched yoki Файл не найден

E-IMZO sertifikat ma’lumotini topgan, ammo dastur mos jismoniy faylni tanlangan papkadan topa olmagan holatlar.

### Metadata unavailable yoki Нет данных о сроке

Sertifikat ma’lumotlarida amal qilish muddati aniqlanmagan holatlar.

Bunday fayllar avtomatik ravishda muddati tugagan deb hisoblanmaydi.

## 8. Muddati tugagan kalitlarni ko‘chirish

### Barcha muddati tugagan kalitlarni ko‘chirish

1. `Expired` yoki `Просроченные` bo‘limini oching.
2. `Move all expired` yoki `Переместить все просроченные` tugmasini bosing.
3. Tasdiqlash oynasini diqqat bilan o‘qing.
4. Amalni tasdiqlang.

Dastur muddati tugagan kalitlarni yangi papkaga ko‘chiradi. Ishlayotgan kalitlar `DSKEYS` papkasida qoladi.

Yangi papka nomi taxminan quyidagicha bo‘ladi:

```text
Expired_Keys_2026-08-14_103000
```

### Faqat tanlangan kalitlarni ko‘chirish

1. `Expired` bo‘limida kerakli qatorlarni tanlang.
2. Bir nechta qatorni tanlash uchun `Ctrl` tugmasini bosib turing.
3. `Move selected expired` tugmasini bosing.
4. Amalni tasdiqlang.

## 9. Kalitni olib tashlash

Kalitni olib tashlash uchun:

1. Kerakli kalit qatorini toping.
2. Qator ustiga sichqonchaning o‘ng tugmasini bosing.
3. `Remove key` yoki `Удалить ключ` bandini tanlang.
4. Tasdiqlash oynasini o‘qing.
5. Amalni tasdiqlang.

Kalit to‘g‘ridan-to‘g‘ri butunlay o‘chirilmaydi. Kalit Windows savatiga yuboriladi.

> Ogohlantirish: ishlayotgan kalitni olib tashlash davlat portallariga kirish imkoniyatini yo‘qotishi mumkin. Faqat holati va nusxasi aniq tekshirilgan kalitlarni olib tashlang.

## 10. Takroriy kalitlar bilan ishlash

1. `Duplicates` yoki `Дубликаты` bo‘limini oching.
2. Bir xil seriya raqamiga ega kalitlarni solishtiring.
3. Fayl joylashuvi va amal qilish muddatini tekshiring.
4. Saqlanadigan asosiy nusxani tanlang.
5. Keraksiz nusxa ustiga o‘ng tugma bilan bosing.
6. `Remove key` bandini tanlang.
7. Amalni tasdiqlang.

Takroriy bo‘limdagi barcha kalitlarni bir vaqtning o‘zida o‘chirish tavsiya etilmaydi. Kamida bitta ishlaydigan nusxa qolishi kerak.

## 11. Fayl joylashuvini ochish

1. Kerakli kalitni tanlang.
2. `Open selected location` yoki `Открыть расположение файла` tugmasini bosing.
3. Windows Explorer fayl joylashgan papkani ochadi.

Bu imkoniyat kalitni qo‘lda tekshirish yoki zaxira nusxa olish uchun foydalidir.

## 12. Xavfsizlik bo‘yicha tavsiyalar

- PFX parolini fayl nomiga yozmang.
- Parolni begona shaxslarga yubormang.
- PFX faylini messenjer yoki ochiq elektron pochta orqali jo‘natmang.
- Kalitlarni o‘chirishdan oldin zaxira nusxa yarating.
- Ishlayotgan kalitni tasodifan o‘chirmang.
- `Metadata unavailable` bo‘limidagi fayllarni tekshirmasdan olib tashlamang.
- `File not matched` bo‘limidagi sertifikatlar uchun papkani qayta tekshiring.
- E-IMZO va Windows tizimini muntazam yangilang.
- Dasturdan faqat ishonchli kompyuterda foydalaning.

## 13. Muammolarni hal qilish

### Dastur ochilmayapti

1. Python 3.13 yoki yangi versiya o‘rnatilganini tekshiring.
2. Buyruqlar oynasida quyidagini bajaring:

```bat
python --version
```

3. `send2trash` kutubxonasini qayta o‘rnating:

```bat
py -m pip install --upgrade send2trash
```

4. Dastur o‘rnatuvchisini qayta ishga tushiring.

### E-IMZO ga ulanmayapti

1. E-IMZO ishlab turganini tekshiring.
2. E-IMZO dasturini to‘liq yoping.
3. E-IMZO dasturini administrator sifatida qayta ishga tushiring.
4. 10 soniya kuting.
5. DFIN DSKEYS Manager ichida qayta skanerlang.
6. ESI.UZ sahifasida kalitlar ko‘rinishini tekshiring.
7. Zarur bo‘lsa, E-IMZO dasturini qayta o‘rnating.

### Dastur o‘qish holatida qolib ketdi

1. 25 soniya kuting.
2. Dastur xato xabarini ko‘rsatishi kerak.
3. E-IMZO dasturini qayta ishga tushiring.
4. `Scan E-IMZO` tugmasini faqat bir marta bosing.
5. Muammo davom etsa, kompyuterni qayta ishga tushiring.

### Kalit fayli topilmadi

1. `C:\DSKEYS` papkasini tekshiring.
2. Dasturda to‘g‘ri papka tanlanganini tekshiring.
3. Kalit boshqa papkada bo‘lsa, `Browse` orqali yangi papkani tanlang.
4. E-IMZO sertifikatni ro‘yxatda ko‘rsatishini tekshiring.

### Kalitlar ro‘yxati bo‘sh

1. E-IMZO ishlayotganini tekshiring.
2. `DSKEYS` papkasida kalitlar mavjudligini tekshiring.
3. Davlat portalidagi ESI.UZ sahifasida kalitlar chiqishini tekshiring.
4. E-IMZO va DFIN DSKEYS Manager dasturlarini qayta ishga tushiring.

## 14. Dasturchilar uchun ishga tushirish

Manba kodini ishga tushirish uchun:

```bat
py DFIN_DSKEYS_Manager.py
```

Kerakli kutubxonani o‘rnatish:

```bat
py -m pip install -r requirements-build.txt
```

Windows o‘rnatuvchisini GitHub Actions orqali yaratish mumkin. Ish jarayoni quyidagi faylda saqlanadi:

```text
.github/workflows/build-windows.yml
```

## 15. Mas’uliyatni cheklash

Dastur kalitlarni boshqarishni yengillashtiradi. Kalitlarni ko‘chirish yoki olib tashlashdan oldin foydalanuvchi ma’lumotlarni tekshirishi va zarur zaxira nusxalarni yaratishi kerak.

DFIN.UZ noto‘g‘ri tanlangan yoki foydalanuvchi tomonidan tasdiqlangan o‘chirish amali natijasida yuzaga kelgan ma’lumot yo‘qolishi uchun javobgar bo‘lmaydi.

## Muallif va loyiha

**DFIN DSKEYS Manager**

**DFIN.UZ tomonidan ishlab chiqilgan**

Rasmiy sayt: `https://www.dfin.uz`
