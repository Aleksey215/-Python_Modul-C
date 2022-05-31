class MyClass():
    def f(self):
        return 155


mc2 = MyClass()
print("it's for test too", mc2.f())

if __name__ == "__main__":
    mc = MyClass()
    print("it's only for test", mc.f())

# Так как мы запускаем файл myclass.py, то оба вывода работают.
# А теперь создадим ситуацию, когда один из них работать не будет. В файл main.py добавим следующий фрагмент кода: