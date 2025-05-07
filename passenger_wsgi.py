import sys, os, site

# 1) Добавляем user‑site‑packages, куда pip3 install --user поставил зависимости
site.addsitedir('/home/b/bobektanym/testter.bobektanym.kz/public_html/.local/lib/python3.10/site-packages')

# 2) Гарантируем, что проектная папка в PATH
sys.path.insert(0, os.path.dirname(__file__))

# 3) Импортируем FastAPI-приложение
from app.main import app as application
