def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap
    return wrapper

class UserUnterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("добавление фильма")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "зежиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
            return dict_article

        @add_title("каталог фильмов")
        def show_all_articles(self, articles):
            for ind, article in enumerate(articles, 1):
                print(f"{ind}. {article}")

        @add_title("Ввод названия фильма")
        def get_user_article(self):
            user_article = input("Введите название фильма: ")
            return user_article

        @add_title("Просмотр фильма")
        def show_single_article(self, article):
            for key in article:
                print(f"{key} фильмы - {article[key]}")