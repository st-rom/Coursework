class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
print(json.dumps(2 + 1j, cls=ComplexEncoder))
print(ComplexEncoder().encode(2 + 1j))
print(list(ComplexEncoder().iterencode(2 + 1j)))
print(json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':')))