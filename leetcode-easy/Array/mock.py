"""
In: (1,2,(5,((((((6)))))),6,7),3,4), function (any) -> True or False
Out: (2,6,6,4)

In: ("A", "B", ("E", "f"), "c"), 
Out: ("A", "B", "E")
  
In: (1,3,5), (any) -> True or False
Out: ()
  
one_dimensionalize((1,2,(5,6,7),3,4), isEven)
"""

def one_dimension(tup, f):
    def _combine(tup, f):
        for item in tup:
            if isinstance(item, tuple):
                _combine(item)
            else:
                if f(item): ls.append(item)
    ls = []
    _combine(tup, f)
    return ls