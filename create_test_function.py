import sublime
import sublime_plugin


class CreateTestFunctionCommand(sublime_plugin.TextCommand):

    """Create a test function for current selected function.
    """

    def run(self, edit):
        count_regions = 0
        for func_name_region in self.view.sel():
            count_regions += 1
            func_name = self.view.substr(func_name_region)
            test_function = self.create_test_function(func_name)

            endline, _ = self.view.rowcol(self.view.size())
            point = self.view.text_point(endline, 0)
            self.view.insert(edit, point, test_function)

        if count_regions == 1:
            if func_name:
                point = self.view.text_point(
                    self.view.rowcol(self.view.size())[0] - 1, 11)
            else:
                point = self.view.text_point(
                    self.view.rowcol(self.view.size())[0] - 2, 9)

            self.view.sel().clear()
            self.view.sel().add(sublime.Region(point))
            self.view.show(point)

    @staticmethod
    def create_test_function(func_name):
        return '\ndef test_{}():\n    assert \n'.format(func_name)
