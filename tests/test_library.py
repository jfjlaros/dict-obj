"""Tests for the dict-obj library."""
from dict_obj import obj


class TestLibrary(object):
    def setup(self):
        self._obj = obj({'a': 1, 'b': {'c': 2}, 'd': ['e', {'f': 'g'}]})

    def test_attr(self):
        assert self._obj.a == 1

    def test_dict(self):
        assert self._obj['a'] == 1

    def test_attr_nest(self):
        assert self._obj.b.c == 2

    def test_mix_nest_1(self):
        assert self._obj['b'].c == 2

    def test_mix_nest_2(self):
        assert self._obj.b['c'] == 2

    def test_dict_nest_3(self):
        assert self._obj['b']['c'] == 2

    def test_attr_assignment_1(self):
        self._obj.e = 10
        assert self._obj.e == 10

    def test_attr_assignment_2(self):
        self._obj.e = 10
        assert self._obj['e'] == 10

    def test_dict_assignment_3(self):
        self._obj['e'] = 10
        assert self._obj.e == 10

    def test_dict_assignment_4(self):
        self._obj['e'] = 10
        assert self._obj['e'] == 10

    def test_attr_assignment_nest_1(self):
        self._obj.e = {'f': 10}
        assert self._obj.e.f == 10

    def test_attr_assignment_nest_2(self):
        self._obj.e = {'f': 10}
        assert self._obj['e'].f == 10

    def test_attr_assignment_nest_3(self):
        self._obj.e = {'f': 10}
        assert self._obj.e['f'] == 10

    def test_attr_assignment_nest_4(self):
        self._obj.e = {'f': 10}
        assert self._obj['e']['f'] == 10

    def test_dict_assignment_nest_1(self):
        self._obj['e'] = {'f': 10}
        assert self._obj.e.f == 10

    def test_dict_assignment_nest_2(self):
        self._obj['e'] = {'f': 10}
        assert self._obj['e'].f == 10

    def test_dict_assignment_nest_3(self):
        self._obj['e'] = {'f': 10}
        assert self._obj.e['f'] == 10

    def test_dict_assignment_nest_4(self):
        self._obj['e'] = {'f': 10}
        assert self._obj['e']['f'] == 10

    def test_attr_list_1(self):
        assert self._obj.d[0] == 'e'

    def test_attr_list_2(self):
        assert self._obj.d[1].f == 'g'

    def test_attr_list_3(self):
        assert self._obj.d[1]['f'] == 'g'

    def test_items(self):
        assert sorted(self._obj.b.items()) == [('c', 2)]

    def test_get_1(self):
        assert self._obj.get('a') == 1

    def test_get_2(self):
        assert self._obj.get('z') == None

    def test_keys(self):
        assert sorted(self._obj.keys()) == ['a', 'b', 'd']

    def test_update(self):
        self._obj.update({'a': 2})
        assert self._obj.a == 2
