import sublime
import sublime_plugin

from .name_converter import CamelcaseToSnakecaseCommand


class CreateTestFunctionCommand(sublime_plugin.TextCommand):

    """Create tests for selected functions/classes.
    """

    def run(self, edit):
        init_endline, _ = self.view.rowcol(self.view.size())
        init_point = self.view.text_point(init_endline + 1, 0)

        for sel in self.view.sel():
            name = self.view.substr(sel)
            test_function = (self.create_test_function_for_class(name, sel)
                             if self.is_class(name)
                             else self.create_test_function_for_function(name))

            endline, _ = self.view.rowcol(self.view.size())
            point = self.view.text_point(endline, 0)
            self.view.insert(edit, point, test_function)

        n_sels = len(self.view.sel())
        self.view.sel().clear()
        if n_sels == 1 and not self.is_class(name):
            if name:
                point = self.view.text_point(self.view.rowcol(
                    self.view.size())[0] - 1, 12 + len(name))
                self.view.sel().add(sublime.Region(point))
            else:
                point = self.view.text_point(self.view.rowcol(
                    self.view.size())[0] - 1, 11 + len(name))
                self.view.sel().add(sublime.Region(point))
                self.view.sel().add(sublime.Region(self.view.text_point(
                    self.view.rowcol(self.view.size())[0] - 2, 9)))
        else:
            self.view.sel().add(sublime.Region(init_point))

        self.view.show(point)

    def create_test_function_for_class(self, class_name, sel):
        instance_name = self._class2instance(class_name)
        methods = self.list_class_methods(sel)
        assertions = ['    assert {}.{}'.format(instance_name, method)
                      + ('' if is_property else '()')
                      + '\n'
                      for method, is_property in methods]
        return ('\ndef test_{}():\n'.format(class_name)
                + '    {} = {}()\n'.format(instance_name, class_name)
                + ''.join(assertions))

    def create_test_function_for_function(self, func_name):
        return ('\ndef test_{}():\n'.format(func_name)
                + '    assert {}()\n'.format(func_name))

    def list_class_methods(self, class_sel):
        class_line = self.view.substr(self.view.line(class_sel))
        class_Indentation = self._get_class_Indentation(class_line)

        following_row = self.view.rowcol(class_sel.begin())[0] + 1

        property_line = ' ' * (class_Indentation + 4) + '@property'
        func_prefix = ' ' * (class_Indentation + 4) + 'def '

        methods = []
        is_property = True
        # A function should be at least two lines long
        while following_row < self.view.rowcol(self.view.size())[0] - 1:
            line = self.view.substr(self.view.line(
                self.view.text_point(following_row, 0)))

            if line == property_line:
                following_row += 1
                next_line = self.view.substr(self.view.line(
                    self.view.text_point(following_row, 0)))
                if next_line.startswith(func_prefix):
                    func_name = next_line.lstrip(func_prefix).split('(')[0]
                    if not func_name.startswith('_'):
                        methods.append((func_name, is_property))
            elif line.startswith(func_prefix):
                func_name = line.lstrip(func_prefix).split('(')[0]
                if not func_name.startswith('_'):
                    methods.append((func_name, not is_property))

            following_row += 1

        return methods

    @staticmethod
    def is_class(name):
        return name[0].isupper()

    @staticmethod
    def _class2instance(class_name):
        return CamelcaseToSnakecaseCommand.camelcase2snakecase(class_name).strip('_')

    @staticmethod
    def _get_class_Indentation(class_line):
        Indentation = 0
        while class_line[Indentation] == ' ':
            Indentation += 1

        return Indentation
