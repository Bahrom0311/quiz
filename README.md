# SQL Quiz Application

Bu loyiha SQL va MySQL bo'yicha test savollarini o'tkazish uchun yaratilgan web ilova.

## O'rnatish

1. Repositoryni klonlang:
```bash
git clone https://github.com/username/quiz-app.git
cd quiz-app
```

2. Virtual environment yarating va faollashtiring:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac uchun
# yoki
venv\Scripts\activate  # Windows uchun
```

3. Kerakli paketlarni o'rnating:
```bash
pip install -r requirements.txt
```

4. Migratsiyalarni o'tkazing:
```bash
python manage.py migrate
```

5. Test ma'lumotlarini import qiling:
```bash
python manage.py import_questions
```

6. Serverni ishga tushiring:
```bash
python manage.py runserver
```

## Imkoniyatlar

- SQL va MySQL bo'yicha test savollar
- Har bir savol uchun alohida tekshirish
- To'g'ri/noto'g'ri javoblarni ko'rsatish
- Umumiy natijani ko'rsatish

## Texnologiyalar

- Django 5.2
- SQLite
- HTML/CSS/JavaScript 