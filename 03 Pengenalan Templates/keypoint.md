## Workflow
1. web browser request data
2. Cek data di urls.py tepatnya dimodul `path('', view.index)`
3. Modul Path akan mengecek function yang diberikan, untuk kasus ini akan mengecek di `views.index`
4. Views.py akan mengambil template menggunakan render `from django.sorcuts import render`
5. Dir template perlu buat file untuk tampilan .html

## Map
> Web Browser (Request) >> urls.py >> views.py >> templates >> .html >> Web Browser (Result)