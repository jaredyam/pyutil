import sublime
import sublime_plugin


class CreateTestFunctionCommand(sublime_plugin.TextCommand):

    """Create a test function for current selected function.
    """

    def run(self, edit):
        func_name = self.view.substr(self.view.sel()[0])
        func_content = self.create_test_function(func_name)
        endline, _ = self.view.rowcol(self.view.size())
        point = self.view.text_point(endline, 0)
        self.view.insert(edit, point, func_content)

        if func_name:
            point = self.view.text_point(*self.view.rowcol(self.view.size()))
        else:
            point = self.view.text_point(self.view.rowcol(self.view.size())[0] - 1,
                                         9)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(point))
        self.view.show(point)

    @staticmethod
    def create_test_function(func_name):
        return 'def test_{}():\n    assert '.format(func_name)
