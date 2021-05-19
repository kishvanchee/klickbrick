from klickbrick import __version__
import unittest
from klickbrick import klickbrick

class TestKlickbrick(unittest.TestCase):

    def test_cli_default_args(self):
        args = klickbrick.parse(['hello'])
        assert args.hello == 'hello'
        assert args.name == 'World'


    def test_cli_named_args(self):
        args = klickbrick.parse(['hello', '--name', 'Kishore'])
        assert args.name == 'Kishore'



    def test_version(self):
        assert __version__ == '0.1.0'
