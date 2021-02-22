import sublime
import sublime_plugin


class NameConverter(sublime_plugin.TextCommand):

    def run(self, edit, converter):
        assert self.view.substr(self.view.sel()[0]), sublime.error_message(
            'expected at least one valid selection')

        selections = [sel for sel in self.view.sel()]
        old_strs = [self.view.substr(sel) for sel in selections]
        new_strs = [converter(s) for s in old_strs]
        for region, new_str in zip(selections, new_strs):
            self.view.replace(edit, region, new_str)


class CamelcaseToSnakecaseCommand(NameConverter):

    """Convert variable names with camelCase to snake_case.
    """

    def run(self, edit):
        super(CamelcaseToSnakecaseCommand, self).run(edit,
                                                     self.camelcase2snakecase)

    @staticmethod
    def camelcase2snakecase(name):
        new_name = []

        for char in name:
            if char.isupper():
                new_name.append('_')
                new_name.append(char.lower())
            else:
                new_name.append(char)

        return ''.join(new_name)


class SnakecaseToCamelcaseCommand(NameConverter):

    """Convert variable names with snake_case to camelCase.
    """

    def run(self, edit):
        super(SnakecaseToCamelcaseCommand, self).run(edit,
                                                     self.snakecase2camelcase)

    @staticmethod
    def snakecase2camelcase(name):
        new_name = []
        need_convert = False

        for char in name:
            if char == '_':
                need_convert = True
                continue

            if need_convert and char != '_':
                new_name.append(char.upper())
                need_convert = False
            else:
                new_name.append(char)

        return ''.join(new_name)
