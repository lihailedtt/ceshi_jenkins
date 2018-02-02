import pytest


class Test_J(object):
    def setup_class(self):
        print('setup_____')
    def teardown_class(self):
        print("teardown_____")

    @pytest.mark.parametrize('a,b',[(1,9),(2,8),(3,7),(4,6),(5,10)])
    def test_j(self,a ,b):
        assert a+b == 10,'失败'