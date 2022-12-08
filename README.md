# Python code 

Advance research 

iterator 

An iterator is an object attached to the 'iterator protocol' — basically this means that it has a next method ('next' by next), which, when called, returns the next 'piece' (or ' item') in the stream and, when there is nothing left to be returned, throws the StopIteration exception.

An iterator object allows you to loop only once. Holds the state (position) of an individual iteration, or, put another way, each loop over a sequence requires an individual iterator object. This means that we can iterate over the same sequence more than once concurrently. Separating the iteration logic from the sequence allows you to have more than one different way to iterate.

Calling the (__iter__)method on a container is the easiest way to have an iterator object. The iter function does that for us, saving us typing time.