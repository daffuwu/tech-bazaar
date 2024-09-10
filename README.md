# Tech Bazaar
## Langkah-langkah mengimplementasikan *checklist* pada tugas 2
- Buat  *virtual environment* dengan menjalankan perintah `python -m venv env` pada direktori yang diiginkan. Misal di direktori `tech-bazaar`.
- Aktifkan *virtual environment* dengan perintah `env\Scripts\activate`.
- Di dalam direktori yang sama, buat berkas `requirements.txt` dan tambahkan beberapa *dependencies*.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
- Lakukan instalasi terhadap *dependencies* yang ada dengan perintah `pip install -r requirements.txt`.
- Buat proyek Django bernama `tech_bazaar` dengan perintah `django-admin startproject tech_bazaar .`.
- Tambahkan kedua string berikut pada `ALLOWED_HOSTS` di `settings.py` untuk keperluan deployment:
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
- Tambahkan juga `'main'` ke dalam daftar aplikasi yang ada sebagai elemen paling terakhir. Daftar aplikasi dapat  diakses pada variabel INSTALLED_APPS.
    ```
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```
- Buat aplikasi dengan nama `main` menggunakan perintah `python manage.py startapp main`. Perhatikan bahwa tercipta direktori baru `main`.
- Buka berkas `models.py` pada direktori aplikasi `main`.
- Isi berkas `models.py` dengan kode berikut.
    ```py
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()

        @property
        def is_expensive(self):
            return self.price>2000
        
        @property
        def is_available(self):
            return self.stock>0

    ```
- Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model.
- Jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal.
- Buka berkas `views.py` yang terletak di dalam berkas aplikasi `main`.
- Isi berkas `views.py` dengan kode berikut.
    ```py
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name' : 'Tech Bazaar',
            'name' : 'Daffa Rayhan Ananda',
            'class' : 'PBP-E'
        }

        return render(request, "main.html", context)

    ```
- Buat direktori `templates` di dalam direktori `main`.
- Buat berkas `main.html` di dalam direktori `templates` dan isilah berkas tersebut dengan teks berikut.
    ```html
    ...
    <h1>Tech Bazaar</h1>

    <h5>App Name: </h5>
    <p>{{ app_name }}</p> 
    <h5>Name: </h5>
    <p>{{ name }}</p> 
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ...
    ```
- Buat berkas `urls.py` di dalam direktori `main`.
- Isi `urls.py` dengan kode berikut.
    ```py
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
- Buka berkas `urls.py` **di dalam direktori proyek `tech_bazaar`, bukan yang ada di dalam direktori aplikasi `main`**.
- Impor fungsi `path` dan `include` dari `django.urls`.
    ```
    ...
    from django.urls import path, include
    ...
    ```
-  Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`.
    ```
    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```
- Pada direktori utama `tech-bazaar` lakukan perintah `git init` untuk menetapkan direktori ini sebagai *repository* lokal.
- Tambahkan berkas `.gitignore` dan isilah berkas tersebut dengan teks berikut.
    ```
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml
    .DS_Store

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod]
    *$py.class

    # Distribution / packaging
    .Python build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    *.manifest
    *.spec

    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .coverage
    .coverage.*
    .cache
    .pytest_cache/
    nosetests.xml
    coverage.xml
    *.cover
    .hypothesis/

    # Jupyter Notebook
    .ipynb_checkpoints

    # pyenv
    .python-version

    # celery
    celerybeat-schedule.*

    # SageMath parsed files
    *.sage.py

    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/

    # mkdocs documentation
    /site

    # mypy
    .mypy_cache/

    # Sublime Text
    *.tmlanguage.cache
    *.tmPreferences.cache
    *.stTheme.cache
    *.sublime-workspace
    *.sublime-project

    # sftp configuration file
    sftp-config.json

    # Package control specific files Package
    Control.last-run
    Control.ca-list
    Control.ca-bundle
    Control.system-ca-bundle
    GitHub.sublime-settings

    # Visual Studio Code
    .vscode/*
    !.vscode/settings.json
    !.vscode/tasks.json
    !.vscode/launch.json
    !.vscode/extensions.json
    .history
    ```
- Akses halaman PWS pada https://pbp.cs.ui.ac.id dan lakukan registrasi menggunakan SSO.
- Buat proyek baru dengan menekan tombol `Create New Project`.
- Isi `Project Name` dengan `techbazaar`. Setelah itu, tekan Create New Project di bawahnya.
- Simpan *credentials* di tempat yang aman.
- Pada `settings.py` di proyek Django yang sudah dibuat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`.
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "daffa-rayhan-techbazaar.pbp.cs.ui.ac.id"]
    ...
    ```
- Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS.