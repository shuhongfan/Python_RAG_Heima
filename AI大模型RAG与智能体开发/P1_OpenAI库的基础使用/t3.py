class Test(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Test({self.name})"

    def __or__(self, other):
        return MySequence(self, other)


class MySequence(object):
    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        return MySequence(*self.sequence + [other])

    def run(self):
        for arg in self.sequence:
            print(arg)


if __name__ == "__main__":
    a = Test("a")
    b = Test("b")
    c = Test("c")

    d = a | b | c
    d.run()
    print(type(d))
