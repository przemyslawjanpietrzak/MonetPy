class MonadLawTester:  # pragma: no cover

    def __init__(self, monad, value, mapper1, mapper2):
        self.monad = monad
        self.value = value
        self.mapper1 = mapper1
        self.mapper2 = mapper2

    def associativity_test(self):
        value1 = self.monad(self.value).bind(self.mapper1).bind(self.mapper2)
        value2 = self.monad(self.value).bind(lambda value: self.mapper2(value).bind(self.mapper1))

        assert value1 == value2

    def left_unit_test(self):
        assert self.monad(self.value).bind(self.mapper1) == self.mapper1(self.value)

    def right_unit_test(self):
        self.monad(self.value).bind(self.mapper1) == self.monad(self.value)

    def test(self, run_associativity_law_test=True, run_left_law_test=True, run_right_law_test=True):
        if run_associativity_law_test:
            self.associativity_test()
        if run_left_law_test:
            self.left_unit_test()
        if run_right_law_test:
            self.right_unit_test()