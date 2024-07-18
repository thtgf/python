from jinja2 import Template
site = [
    {'id':1,'index':'Главная'},
    {'id':2,'news':'Новости'},
    {'id':3,'about':'О компании'},
    {'id':4,'shop':'Магазин'},
    {'id':5,'contacts':'Контакты'},
]
link ="""<ul>
<li><a href="/index" class="active">Главная</a></li>
<li><a href="/news">Новости</a></li>
<li><a href="/about">О компании</a></li>
<li><a href="/shop">Магазин</a></li>
<li><a href="/contacts">Контакты</a></li>
</ul>"""
print(link)