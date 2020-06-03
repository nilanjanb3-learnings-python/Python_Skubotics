Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[20,15,40,10,50,90,105,5]
>>> l.max()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l.max()
AttributeError: 'list' object has no attribute 'max'
>>> max(l)
105
>>> _+100
205
>>> c=6+5j
>>> type(c)
<class 'complex'>
>>> a=10
>>> b=15
>>> d=b>a
>>> typr(d)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    typr(d)
NameError: name 'typr' is not defined
>>> type(d)
<class 'bool'>
>>> d=a>b
>>> type(d)
<class 'bool'>
>>> d
False
>>> d=b>a
>>> d
True
>>> c=15.13245
>>> type(c)
<class 'float'>
>>> d=float(c)
>>> d
15.13245
>>> d=int(c)
>>> d
15
>>> c="Nilanjan"
>>> type(c)
<class 'str'>
>>> d=int(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d=int(c)
ValueError: invalid literal for int() with base 10: 'Nilanjan'
>>> range(0,10)
range(0, 10)
>>> 
>>> range()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    range()
TypeError: range expected 1 arguments, got 0
>>> c=(range(0,10))
>>> c
range(0, 10)
>>> c=range[0,10]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c=range[0,10]
TypeError: 'type' object is not subscriptable
>>> c=[range[0,10]]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c=[range[0,10]]
TypeError: 'type' object is not subscriptable
>>> c={52,5,10,14,23,54,78}
>>> c
{5, 10, 14, 78, 52, 54, 23}
>>> type(c)
<class 'set'>
>>> c.add({5,10})
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c.add({5,10})
TypeError: unhashable type: 'set'
>>> c.add(10)
>>> c
{5, 10, 14, 78, 52, 54, 23}
>>> c.add(4,12)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c.add(4,12)
TypeError: add() takes exactly one argument (2 given)
>>> c.add(4)
>>> c
{4, 5, 10, 14, 78, 52, 54, 23}
>>> c.clear(4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c.clear(4)
TypeError: clear() takes no arguments (1 given)
>>> c.clear()
>>> c
set()
>>> c
set()
>>> c={12,14,78,52,46,12,56,45,12,19,72}
>>> c
{72, 12, 45, 46, 78, 14, 19, 52, 56}
>>> c.update({554,5244})
>>> c
{72, 554, 12, 45, 46, 78, 14, 19, 52, 56, 5244}
>>> c.difference()
{72, 554, 12, 45, 46, 78, 14, 19, 52, 56, 5244}
>>> b={72,12}
>>> c.difference(b)
{554, 45, 78, 46, 14, 19, 52, 56, 5244}
>>> c.difference_update(b)
>>> c
{554, 45, 46, 78, 14, 19, 52, 56, 5244}
>>> c.discard({46,78})
>>> c
{554, 45, 46, 78, 14, 19, 52, 56, 5244}
>>> c.discard(0)
>>> c
{554, 45, 46, 78, 14, 19, 52, 56, 5244}
>>> c.discard()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c.discard()
TypeError: discard() takes exactly one argument (0 given)
>>> c.discard(45)
>>> c
{554, 46, 78, 14, 19, 52, 56, 5244}
>>> c.remove({46,14})
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    c.remove({46,14})
KeyError: {46, 14}
>>> c.remove{46}
SyntaxError: invalid syntax
>>> c.remove(46)
>>> c
{554, 78, 14, 19, 52, 56, 5244}
>>> c=list[range(0,10)]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    c=list[range(0,10)]
TypeError: 'type' object is not subscriptable
>>> c=list(range(0,10))
>>> c
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #Dictionary
>>> c=('N':'7699824219','S':'7699824219')
SyntaxError: invalid syntax
>>> c={'N':'7699824219','S':'7699824219'}
>>> c.get(N)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    c.get(N)
NameError: name 'N' is not defined
>>> c.get("N")
'7699824219'
>>> c.get("S")
'7699824219'
>>> c.keys()
dict_keys(['N', 'S'])
>>> c.values()
dict_values(['7699824219', '7699824219'])
>>> a=10
>>> b=15
>>> a>b
False
>>> b>a
True
>>> a==b
False
>>> a!=b
True
>>> c=((a>b)&(b>a))
>>> c
False
>>> c=((a>b)|(b>a))
>>> c
True
>>> c=((a>b)or(b>a))
>>> c
True
>>> a=-a
>>> a
-10
>>> a=-a
>>> a
10
>>> a+=a
>>> a
20
>>> _-10
10
>>> a
20
>>> a-=a
>>> a
0
>>> a+10=a
SyntaxError: can't assign to operator
>>> a
0
>>> a=_+10
>>> a
10
>>> (a,b)=(b,a)
>>> a
15
>>> b
10
>>> (a,b)=(b,a)
>>> a
10
>>> b
15
>>> #Swaping of two digits
>>> c=32
>>> digit1=c//10
>>> digit2=c%10
>>> d=digit2*10+digit1
>>> d
23
>>> 
