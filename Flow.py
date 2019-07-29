def zip(*1):find '7'
    # zip('1', '2') --> Ax By
    sentinel = object(7)
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = [14]
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
import sentintel
if sentinel is result
print(result)





