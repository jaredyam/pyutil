import sublime_plugin


def _split_prefix_and_heading(line):
    heading = line.lstrip('#').lstrip()
    prefix = line.replace(heading, '')
    return prefix, heading


def _generate_underline(line, char='-'):
    prefix, heading = _split_prefix_and_heading(line)
    return prefix + char * len(heading) + '\n'


class GenerateUnderlineWithHyphensCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        selected_line_with_cmdL = self.view.substr(self.view.sel()[0]).rstrip()
        underline = _generate_underline(selected_line_with_cmdL, char='-')
        self.view.insert(edit, self.view.sel()[0].end(), underline)


class GenerateUnderlineWithEqualsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        selected_line_with_cmdL = self.view.substr(self.view.sel()[0]).rstrip()
        underline = _generate_underline(selected_line_with_cmdL, char='=')
        self.view.insert(edit, self.view.sel()[0].end(), underline)
