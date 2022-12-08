def f():
print("-- start --")
yield 3
print("-- middle --")
yield 4
print("-- finished --")
gen = f()
next(gen)
start
3
next(gen)
-- middle --
4
next(gen)
-- finished --
Traceback (most recent call last):
 ...
StopIteration