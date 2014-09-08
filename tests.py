import unittest

from save_file_syntax import Hashes
from save_file_syntax import SaveFile

class Primitive_tests(unittest.TestCase):
    def test_yes(self):
        test_string = '''test=
        {
            should_be_true=yes
            should_be_false=no
        }'''

        result = Hashes.parseString(test_string)

        self.failUnless(result["test"]["should_be_true"] == True)

    def test_no(self):
        test_string = '''test=
        {
            should_be_true=yes
            should_be_false=no
        }'''

        result = Hashes.parseString(test_string)

        self.failUnless(result["test"]["should_be_false"] == False)
git
class Hashes_tests(unittest.TestCase):

    def test_single_key_with_string_value(self):
        test_string = '''
            date="1454.1.1"
            thing="stuff"'''

        result = Hashes.parseString(test_string)

        self.failUnless(result["thing"] == "stuff")

    def test_header_and_keys(self):
        test_string = '''EU4txt
            date="1454.1.1"
            player="TUR"'''

        result = SaveFile.parseString(test_string)

        self.failUnless(result["player"] == "TUR")

    def test_curly_brace_sub_dict(self):
        test_string = '''player="TUR"
            savegame_version=
            {
                first=1
                second=7
                third=3
                forth=0
            }'''

        result = Hashes.parseString(test_string)

        self.failUnless(result["savegame_version"]["second"] == 7)

    def test_curly_brace_sub_list(self):
        test_string = '''gameplaysettings=
            {
                setgameplayoptions=
                {
                    1 1 0 0 0 0 0 1 0 1 0 0 
                }
            }'''

        result = Hashes.parseString(test_string)

        self.failUnless(result["gameplaysettings"]["setgameplayoptions"][1] == 1)


if __name__ == '__main__':
    unittest.main()

