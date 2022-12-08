>>> nums = [1,2,3]      #
>>> iter(nums)
<listiterator object at ...>
>>> nums.__iter__()
<listiterator object at ...>
>>> nums.__reversed__()
<listreverseiterator object at ...>
>>>
>>> it = iter(nums)
>>> next(it)            # next(obj) called as obj.next()
1
>>> it.next()
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration