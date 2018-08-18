"""Tests for the dict-obj CLI."""
import StringIO

from dict_obj import dict_obj

from shared import md5_check


class TestCLI(object):
    def setup(self):
        self._output = StringIO.StringIO()

    def _md5_check(self, md5sum):
        return md5_check(self._output.getvalue(), md5sum)

    def test_1(self):
        pass
