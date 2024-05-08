class Clock:
    __DAY = 86400  # Число секунд в дне

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

        def get_format_time(self):
            s = self.sec % 60
            m = (self.sec // 60) % 60
            h = (self.sec // 3600) % 24
            return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

        @staticmethod
        def __get_form(x):
            return str(x) if x > 9 else "0" + str(x)
        def __getitem__(self, item):
            if not isinstance(item, str):
                raise ValueError("Ключ должен быть строкой")
            if item == "hour":
                return self.sec // 3600 % 24
            if item == "min":
                return self.sec // 60 % 60
            if item == "sec":
                return self.sec % 60
            c1 = Clock(80000)
            print(c1.get_format_time())
            print(c1["hour"], c1["min"], c1["sec"])
