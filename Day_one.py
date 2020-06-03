Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 2*3
6
>>> 3-2
1
>>> 3/2
1.5
>>> 3//2
1
>>> 3%2
1
>>> 5%3
2
>>> 5//3
1
>>> 5/3
1.6666666666666667
>>> 2**3
8
>>> 2**10
1024
>>> "Hello"
'Hello'
>>> 'Hello'
'Hello'
>>> print("Hello World")
Hello World
>>> print("Nilanjan's Laptop")
Nilanjan's Laptop
>>> print('Nilanajn's Laptop')
      
SyntaxError: invalid syntax
>>> print('Nilanajan\'s Laptop')
Nilanajan's Laptop
>>> print("Hello" + "World")
HelloWorld
>>> print(10*"Nilanjan")
NilanjanNilanjanNilanjanNilanjanNilanjanNilanjanNilanjanNilanjanNilanjanNilanjan
>>> print(10*"Nilanjan\n")
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan
Nilanjan

>>> print(r"C:\n")
C:\n
>>> x=10
>>> y=15
>>> x+y
25
>>> y-x
5
>>> x+y
25
>>> _+10
35
>>> a
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> name="Nilanjan"
>>> surname="Bhattacharjee"
>>> print("My Name is "+"name "+"surname")
My Name is name surname
>>> print("My Name Is " name + surname)
SyntaxError: invalid syntax
>>> print(name)
Nilanjan
>>> print(name+surname)
NilanjanBhattacharjee
>>> print("Name is "+name+surname)
Name is NilanjanBhattacharjee
>>> name[0]
'N'
>>> name[3]
'a'
>>> name[-1]
'n'
>>> len(name)
8
>>> name[1:3]
'il'
>>> name[0:3]
'Nil'
>>> name[0:]
'Nilanjan'
>>> name[:8]
'Nilanjan'
>>> nums=[90,10,50,40,30]
>>> nums
[90, 10, 50, 40, 30]
>>> nums[2]
50
>>> nums[0:3]
[90, 10, 50]
>>> nums.insert[2:20]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    nums.insert[2:20]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.insert[2,20]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    nums.insert[2,20]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.insert(2,20)
>>> nums
[90, 10, 20, 50, 40, 30]
>>> nums.remove(40)
>>> nums
[90, 10, 20, 50, 30]
>>> nums.remove(10,20)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    nums.remove(10,20)
TypeError: remove() takes exactly one argument (2 given)
>>> del nums(1)
SyntaxError: can't delete function call
>>> del nums[1]
>>> nums
[90, 20, 50, 30]
>>> nums.insert(10,20)
>>> nums
[90, 20, 50, 30, 20]
>>> del nums[0:2]
>>> nums
[50, 30, 20]
>>> nums.pop(1)
30
>>> nums.pop()
20
>>> nums.extend([20,30,40,50])
>>> nums
[50, 20, 30, 40, 50]
>>> nums.remove([30,40])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    nums.remove([30,40])
ValueError: list.remove(x): x not in list
>>> nums.sort()
>>> nums
[20, 30, 40, 50, 50]
>>> nums.reverse()
>>> nums
[50, 50, 40, 30, 20]
>>> nums.sort()
>>> nums
[20, 30, 40, 50, 50]
>>> x=10
>>> x
10
>>> type(x)
<class 'int'>
>>> char='Nilanjan'
>>> type(char)
<class 'str'>
>>> id(x)
1846699328
>>> id(char)
61875968
>>> 
