# UpTrader_test_task

### Тестовое задание от компании UpTrader

### TASK: 

#### 1) Меню реализовано через template tag

✅ Реализовано по средствам inclusion_tag()

#### 2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.

✅ Выделенный пункт меню и все его подуровень развернуты.

![Снимок экрана 2023-04-03 082209](https://user-images.githubusercontent.com/113121885/229418370-84aefb0b-d24f-48b3-b35b-6a4683f1066c.png)

#### 3) Хранится в БД.
✅ Меню хранится в базе данных SQLite3, что позволяет легко изменять его содержимое через стандартную админку Django.

#### 4) Редактируется в стандартной админке Django

✅ В админке есть возможность настроить родительский элемент для каждого пункта выпадающего меню. Таким образом, администратор сайта может легко изменять содержимое меню, без необходимости редактировать шаблон.

#### 5) Активный пункт меню определяется исходя из URL текущей страницы

✅ Исходя из URL адреса текущий пункт меню становится активным, что позволяет пользователю всегда знать, на какой странице он находится.

#### 6) Меню на одной странице может быть несколько. Они определяются по названию.

✅ На главной странице реализована возможность выбрать нужный пункт меню.

#### 7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.

✅  

#### 8) На отрисовку каждого меню требуется ровно 1 запрос к БД


✅ На отрисовку каждого меню требуется ровно 1 запрос к БД, что позволяет обеспечивать быстрое отображение меню на сайте, даже при большом количестве пунктов.
