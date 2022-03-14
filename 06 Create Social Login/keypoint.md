# Library
> **Django Allauth** https://django-allauth.readthedocs.io/en/latest/installation.html 

# Important Migration
1. `python manage.py makemigrations`
2. `python manage.py migrate`

# Create Username login admin
1. `python manage.py createsuperuser`
2. **make a super user**

# Create Gmail API
1. >Follow link: https://console.cloud.google.com/
2. Select project and search *gmail api*
3. Select menu **Credentials**
4. *Create Credentials >>  Create OAuth client ID >> configuration consent screen >> create >> fill important >> save & continue*
5. Again, select menu **Credentials**
6. *Create Credentials >>  Create OAuth client ID >> fill important things >> create*
7. Successfull create **Client id & Secret key** for **Django administration**
8. Settings OAuth 2.0 Client IDs for *Authorized JavaScript origins &  Authorized redirect URIs*
>*Authorized redirect URIs*
- `http://127.0.0.1:8000/accounts/google/login/callback/`
- `http://localhost:8000/accounts/google/login/callback/`
>*Authorized JavaScript origins*
- `http://127.0.0.1:8000`
- `http://localhost:8000`