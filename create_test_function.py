import sublime
import sublime_plugin

from .name_converter import CamelcaseToSnakecaseCommand


class CreateTestFunctionCommand(sublime_plugin.TextCommand):

    """Create tests for selected functions/classes.
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

        # if there is only one test being created, move cursor to the proper
        # position
        if count_regions == 1:
            if func_name:
                point = self.view.text_point(
                    self.view.rowcol(self.view.size())[0] - 1, 12 + len(func_name))
            else:
                point = self.view.text_point(
                    self.view.rowcol(self.view.size())[0] - 2, 9)

            self.view.sel().clear()
            self.view.sel().add(sublime.Region(point))
            self.view.show(point)

    def create_test_function(self, name):
        # consider both the class case and the function case
        test_func_name = 'test_{}'.format(
            CamelcaseToSnakecaseCommand.camelcase2snakecase(name).strip('_'))

        return '\ndef {}():\n    assert {}()\n'.format(test_func_name, name)
