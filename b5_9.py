import time


class Stopwatch:
    """
    Создаем класс, который можно будет использовать в качестве контекстного менеджера
    """
    def __call__(self, num_runs=5):
        """
        Переопределяем функцию вызова объекта класса,
        который принимает количество запусков секундомера в качестве опционального аргумента,
        значение по-умолчанию = 5
        """
        def decorator(func):
            def wrap():
                avg_time = 0
                for _ in range(num_runs):
                    t0 = time.time()
                    func()
                    t1 = time.time()
                    avg_time += (t1 - t0)
                avg_time /= num_runs
                return avg_time
            return wrap
        return decorator

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Stopwatch() as time_this:
    #Задаем количество прогонов функции = 10
    @time_this(num_runs=10)
    def f():
        for j in range(1000000):
            pass

print("Время выполнения функции %.5f секунд"%f())