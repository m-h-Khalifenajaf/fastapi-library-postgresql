# FastAPI Book Management API with PostgreSQL

## 1. Description

This project is a REST API for managing books, developed using FastAPI and PostgreSQL. It supports creating, retrieving, updating, and deleting books.

The application uses Psycopg to connect directly to PostgreSQL without using an ORM or Pydantic.

## 2. Technologies

- Python
- FastAPI
- PostgreSQL
- Psycopg 3

## 3. Requirements

- Python installed
- PostgreSQL installed and running
- A database named `library_db`
- A table named `books`

### Database Table Structure

```sql
CREATE TABLE books (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);
```

The table stores each book's ID, title, and author.

## 4. Installation

Install the required dependencies by running the following command in the project directory:

```powershell
python -m pip install -r requirements.txt
```

## 5. Database Configuration

The application uses the following PostgreSQL connection settings:

- Host: `localhost`
- Port: `5432`
- Database: `library_db`
- Username: `postgres`
- Password: Read from the `DB_PASSWORD` environment variable.

Set the database password in PowerShell before running the application:

```powershell
$env:DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
```

Replace `YOUR_POSTGRES_PASSWORD` with your actual PostgreSQL password.

**Security Note:** Do not commit your actual database password to Git.

## 6. Running the Application

Start the development server using:

```powershell
fastapi dev main.py --port 8001
```

Open the interactive API documentation at:

http://127.0.0.1:8001/docs

## 7. API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Retrieve all book titles |
| POST | `/books` | Create a new book |
| GET | `/books/{id_book}` | Retrieve a book by ID |
| PATCH | `/books/{id_book}` | Update a book's title or author |
| DELETE | `/books/{id_book}` | Delete a book by ID |

### Endpoint Details

**GET `/books`**

Returns a list of all book titles.

**POST `/books`**

Creates a new book using the `title_new_book` and `author_new_book` parameters.

**GET `/books/{id_book}`**

Returns the title and author of the requested book.

**PATCH `/books/{id_book}`**

Updates the title, author, or both. The `title` and `author` parameters are optional.

**DELETE `/books/{id_book}`**

Deletes the specified book from the database.

## 8. Error Handling

If a requested book does not exist, the API returns an HTTP `404 Not Found` response.

## 9. Data Storage

Book information is stored in PostgreSQL. The data persists after the application stops or restarts.

---

# رابط برنامه‌نویسی مدیریت کتاب با FastAPI و PostgreSQL

## ۱. توضیحات پروژه

این پروژه یک REST API برای مدیریت کتاب‌ها است که با استفاده از FastAPI و PostgreSQL توسعه داده شده است. این برنامه امکان ثبت، دریافت، ویرایش و حذف کتاب‌ها را فراهم می‌کند.

برای اتصال مستقیم به PostgreSQL از کتابخانه Psycopg استفاده شده است و در این پروژه از ORM یا Pydantic استفاده نمی‌شود.

## ۲. فناوری‌های استفاده‌شده

- Python
- FastAPI
- PostgreSQL
- Psycopg 3

## ۳. پیش‌نیازها

- نصب بودن Python
- نصب و فعال بودن PostgreSQL
- ایجاد پایگاه داده‌ای با نام `library_db`
- ایجاد جدولی با نام `books`

### ساختار جدول پایگاه داده

```sql
CREATE TABLE books (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);
```

این جدول شناسه، عنوان و نویسنده هر کتاب را ذخیره می‌کند.

## ۴. نصب وابستگی‌ها

برای نصب کتابخانه‌های موردنیاز، دستور زیر را در پوشه پروژه اجرا کنید:

```powershell
python -m pip install -r requirements.txt
```

## ۵. تنظیمات پایگاه داده

برنامه برای اتصال به PostgreSQL از تنظیمات زیر استفاده می‌کند:

- میزبان: `localhost`
- درگاه: `5432`
- نام پایگاه داده: `library_db`
- نام کاربری: `postgres`
- رمز عبور: از متغیر محیطی `DB_PASSWORD` خوانده می‌شود.

پیش از اجرای برنامه، رمز عبور پایگاه داده را در PowerShell تنظیم کنید:

```powershell
$env:DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
```

عبارت `YOUR_POSTGRES_PASSWORD` را با رمز عبور واقعی PostgreSQL جایگزین کنید.

**نکته امنیتی:** رمز عبور واقعی پایگاه داده را در Git ثبت نکنید.

## ۶. اجرای برنامه

برای اجرای سرور توسعه، دستور زیر را وارد کنید:

```powershell
fastapi dev main.py --port 8001
```

برای مشاهده مستندات تعاملی API به آدرس زیر مراجعه کنید:

http://127.0.0.1:8001/docs

## ۷. مسیرهای API

| متد HTTP | مسیر | توضیحات |
|---|---|---|
| GET | `/books` | دریافت عنوان تمام کتاب‌ها |
| POST | `/books` | ثبت کتاب جدید |
| GET | `/books/{id_book}` | دریافت اطلاعات کتاب بر اساس شناسه |
| PATCH | `/books/{id_book}` | ویرایش عنوان یا نویسنده کتاب |
| DELETE | `/books/{id_book}` | حذف کتاب بر اساس شناسه |

### جزئیات مسیرها

**GET `/books`**

فهرستی از عنوان تمام کتاب‌ها را برمی‌گرداند.

**POST `/books`**

با استفاده از پارامترهای `title_new_book` و `author_new_book` یک کتاب جدید ثبت می‌کند.

**GET `/books/{id_book}`**

عنوان و نویسنده کتاب موردنظر را بر اساس شناسه برمی‌گرداند.

**PATCH `/books/{id_book}`**

عنوان، نویسنده یا هر دو را ویرایش می‌کند. پارامترهای `title` و `author` اختیاری هستند.

**DELETE `/books/{id_book}`**

کتاب مشخص‌شده را از پایگاه داده حذف می‌کند.

## ۸. مدیریت خطا

اگر کتاب موردنظر وجود نداشته باشد، API پاسخ HTTP با کد `404 Not Found` برمی‌گرداند.

## ۹. ذخیره‌سازی اطلاعات

اطلاعات کتاب‌ها در PostgreSQL ذخیره می‌شوند؛ بنابراین پس از توقف یا راه‌اندازی مجدد برنامه، اطلاعات در پایگاه داده باقی می‌مانند.
