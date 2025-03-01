import unittest
from pynversify import Container, injectable

@injectable
class Dummy:
    def __init__(self):
        self.value = 42

class TestInversify(unittest.TestCase):
    def test_dummy_binding(self):
        container = Container()
        container.bind(Dummy).toSelf().inSingletonScope()
        dummy1 = container.get(Dummy)
        dummy2 = container.get(Dummy)
        self.assertEqual(dummy1.value, 42)
        self.assertIs(dummy1, dummy2)

if __name__ == '__main__':
    unittest.main()
