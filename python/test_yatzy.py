from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance():
        data_1 = Yatzy.chance(1, 1, 3, 3, 6)
        data_2 = Yatzy.chance(4, 5, 5, 6, 1)
        expected_chance_1 = 14
        expected_chance_2 = 21

        assert data_1 == expected_chance_1
        assert data_2 == expected_chance_2

def test_yatzy_should_return_50():
        data = Yatzy.yatzy([1, 1, 1, 1, 1])
        assert data == 50

def test_yatzy_should_return_0():
        data = Yatzy.yatzy([1, 1, 2, 1, 1])
        assert data == 0

def test_ones():
        data = Yatzy.ones(1, 1, 2, 4, 4)
        assert data == 2
