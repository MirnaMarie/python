Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = float(input('Введите произвольное число: '))
... border = float(input('Введите пограничное число: '))
...  
... if border * 3 <= num:
...      print("Произвольное число больше пограничного в 3 раза")
... elif num > border:
...      print("Произвольное число "+ "%.0f" % num + " больше, чем пограничное " + "%.0f" % border)
... else:
...      print("Произвольное число "+ "%.0f" % num + " меньше, чем пограничное " + "%.0f" % border)
... 
