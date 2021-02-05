import sublime_plugin


def _split_prefix_and_heading(line):
    heading = line.lstrip('#').lstrip()
    prefix = line.replace(heading, '')
    return prefix, heading


def _generate_underline(line, char='-'):
    prefix, heading = _split_prefix_and_heading(line)
    return prefix + char * len(heading) + '\n'


class GenerateUnderline(sublime_plugin.TextCommand):

    def run(self, edit, char='-'):
        rows = [self.view.rowcol(selected_line_with_cmdL_or_cursor.begin())[0]
                for selected_line_with_cmdL_or_cursor in self.view.sel()]
        lines = [self.view.substr(self.view.full_line(self.view.text_point(row, 0))).rstrip()
                 for row in rows]
        for i, line in enumerate(lines):
            underline = _generate_underline(line, char=char)
            self.view.insert(edit,
                             self.view.text_point(rows[i] + 1 + i, 0),
                             underline)


class GenerateUnderlineWithHyphensCommand(GenerateUnderline):

    def run(self, edit):
        super(GenerateUnderlineWithHyphensCommand,
              self).run(edit, char='-')


class GenerateUnderlineWithEqualsCommand(GenerateUnderline):

    def run(self, edit):
        super(GenerateUnderlineWithEqualsCommand,
              self).run(edit, char='=')


class GenerateUnderlineWithRightAngleBracketsCommand(GenerateUnderline):

    def run(self, edit):
        super(GenerateUnderlineWithRightAngleBracketsCommand,
              self).run(edit, char='>')
