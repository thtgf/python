
html = '''
{% macro input(name, type,placeholder) -%}
<input type="{{type}}" name="{{name}}"placeholder="{{placeholder}}>
{%- endmacro %}
<p><input type="text" name="firstname" placeholder ="Имя"></p>
<p><input type ="text" name="lastname" placeholder="Фамилия"></p>
<p><input type ="text" name="address" placeholder="Адрес"></p>
<p><input tipe ="tel" name="phone" placeholder ="Телефон"></p>
<p><input tipe ="text" name ="email" placeholder ="Почта"></p>
'''
print(html)