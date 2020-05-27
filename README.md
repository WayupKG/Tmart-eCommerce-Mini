# Tmart-eCommerce-Mini
Это приложение мини интернет-магазина на основе Django

# Инструкция 

1) ### Инструкция
  Убедитесь, что Python версии 3 установлен на вашем компьютере или ноутбуке.<br>
  Установка Python3 на [Windows](https://www.youtube.com/watch?v=IU4-19ofajg), []()
 	 <br>
  **Git clone** <br>
  `>>> https://github.com/WayupKG/Tmart-eCommerce-Mini.git`<br>
  `>>> cd Tmart`
  
2) ### Установка виртуального окружения
  Убедитесь, что virtualenv установлен на вашем компьютере или ноутбуке.<br>
  `>>> python3 -m venv venv`<br>
  `>>> source venv/bin/activate`
  
3) ### Установка зависимостей
  Он установит все необходимые зависимости в проекте.<br>
  `>>> pip3 install -r requirements.txt`
  
3) ### Миграции 
  Для запуска миграций. <br>
  `>>> python manage.py makemigrations`<br>
  `>>> python manage.py migrate`
  
4) ### Создание суперпользователя
  Для создания суперпользователя напишите команду. <br>
  `>>> python manage.py createsuperuser` <br>
  После выполнения этой команды она запросит имя пользователя и пароль.
  Вы можете получить доступ к панели администратора из `localhost:8000/admin/`

4) ### Запуск проекта
   Он будет работать на порту 8000 по умолчанию.<br>
  `>>> python manage.py runserver` 
  
