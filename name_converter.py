import sublime_plugin


class CamelcaseToSnakecaseCommand(sublime_plugin.TextCommand):

    """Convert function/variable name with camelCase to snake_case.
    """

    def run(self, edit):
        selected_text = self.view.substr(self.view.sel()[0])
        changed_text = self.camelcase2snakecase(selected_text)
        self.view.replace(edit, self.view.sel()[0], changed_text)

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


class SnakecaseToCamelcaseCommand(sublime_plugin.TextCommand):

    """Convert function/variable name with snake_case to camelCase.
    """

    def run(self, edit):
        selected_text = self.view.substr(self.view.sel()[0])
        changed_text = self.snakecase2camelcase(selected_text)
        self.view.replace(edit, self.view.sel()[0], changed_text)

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
