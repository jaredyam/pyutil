import sublime
import sublime_plugin


def _split_prefix_and_heading(line):
    heading = line.lstrip('#').lstrip()
    prefix = line.replace(heading, '')
    return prefix, heading


class GenerateUnderline(sublime_plugin.TextCommand):

    def run(self, edit, char='-'):
        rows = [self.view.rowcol(sel.begin())[0] for sel in self.view.sel()]
        lines = [self.view.substr(self.view.full_line(self.view.text_point(row, 0))).rstrip()
                 for row in rows]
        for i, line in enumerate(lines):
            prefix, heading = _split_prefix_and_heading(line)
            self.view.insert(edit,
                             self.view.text_point(rows[i] + 1 + 2 * i, 0),
                             (prefix + char * len(heading)
                              + '\n' + prefix
                              + '\n'))
            if i == 0:
                point = self.view.text_point(rows[0] + 2, len(prefix))
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(point))
                self.view.show(point)


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
