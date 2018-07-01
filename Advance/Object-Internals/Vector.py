# class Vector:

#     def __init__(self, **coords):
#         # auto add attributes follow list in the coords
#         # alter define attribute manual
#         self.__dict__.update(coords)
    
#     def __repr__(self):
#         return "{}({})".format(
#             self.__class__.__name__,
#             ', '.join("{k}={v}".format(
#                 k = k,
#                 v = self.__dict__[k])
#                 for k in sorted(self.__dict__.keys())
#             )
#         )

class Vector:

    def __init__(self, **coords):
        private_coords = {'_'+ k : v for k,v in coords.items()}
        # auto add attributes follow list in the coords
        # alter define attribute manual
        self.__dict__.update(private_coords)
    
    def __getattr__(self, name):
        # print("name = ", name)
        private_name = '_' + name
        try:
            return self.__dict__[private_name]
        except KeyError:
            #if private_name not in self.__dict__:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                self.__class__, name))
        #return getattr(self, private_name)

    def __setattr__(self, name, value):
        # In str.format, !s chooses to use str to format the object
        # whereas !r chooses repr to format the value.
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k = k[1:],
                v = self.__dict__[k])
                for k in sorted(self.__dict__.keys())
            )
        )

class ColoredVector(Vector):
    COLOR_INDEXED = ('red', 'green', 'blue')

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        self.__dict__['color'] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXED.index(name)
        except ValueError:
            return super().__getattr__(name)
        else: 
            return self.__dict__['color'][channel]
    
    def __repr__(self):
        keys = set(self.__dict__.keys())
        keys.discard('color')
        coords = ', '.join(
            "{k}={v}".format(k=k[1:], v = self.__dict__[k])
            for k in sorted(keys)
        )

        # print(coords)
        return "{cls}({red}, {green}, {blue}, {coords})".format(
            cls = self.__class__.__name__,
            red = self.red,
            green = self.green,
            blue = self.blue,
            coords = coords
        )


if __name__ == '__main__':
    cv = ColoredVector(red = 50, green =100, blue = 200, p = 1, q =2)
    print("{cv}")