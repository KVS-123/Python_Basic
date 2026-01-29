
class MyDict(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 0


a = MyDict()
a[1] = '123'
print(a.get(1))
print(a.get(2))
