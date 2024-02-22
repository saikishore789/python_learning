Yeild:
In order to understand what yield does, we must first understand how generators work. And to understand generators, we must understand what iterables and iterators are.

For example, consider a staircase. A staircase has steps, and the way you climb the staircase is by climbing the steps one by one until you reach the top.

An alternative way of climbing the stairs is to take several steps at a time. You may take two, three, or even four steps at a time, depending on the length of your legs. The length of your legs here is the limitation. If the staircase is longer than your legs, you are forced to climb the staircase in chunks.

In programming, the limitation is your computer’s memory.

If small list and most computers’ memories can store it without any problem. But if we are working with significant amounts of data, reading a large file for example, your computer may not be able to store the data in its memory.

Generator functions are a solution to overcome this limitation. By generating values on the fly, generators allow you to handle large datasets with minimal consumption of memory and processing cycles.

Just like going over a staircase in chunks when the staircase is longer than your legs.

Now that we have an intuitive understanding, let’s learn more.

Iterables
In Python, all sequence types (lists, tuples, and strings) and some container objects (dictionaries, sets, and file objects) are like staircases. You can visit each element one by one. These are called iterables. Iterables contain a countable number of values that are stored in memory.

Iterators

An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().

When you use a for loop to iterate over an iterable like a list, the iterable object is passed to the built-in iter() function (different from `iter()), which returns an iterator object. Although the iterable object contains the items, the iterator object keeps track of which item is next to be used in a loop.

Generator Functions
Generator functions are a special kind of function that return a lazy iterator called a generator iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

A generator iterator generates and returns a value on each call of its __next__() method. When the object runs out of values to return, it raises a StopIteration exception.

The yield Keyword

The yield keyword in Python controls the flow of a generator function. This is similar to a return statement used for returning values in Python. However, there is a difference.

When you call a function that has a yield statement, as soon as a yield is encountered, the execution of the function halts and returns a generator iterator object instead of simply returning a value. The state of the function, which includes variable bindings, the instruction pointer, the internal stack, and a few other things, is saved.

In other words, the yield keyword will convert an expression that is specified along with it to a generator iterator, and return it to the caller.

If you want to get the values stored inside the generator object, you need to iterate over it. You can iterate over it using for loops or special functions like next().