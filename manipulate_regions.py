import sublime
import sublime_plugin


class SplitIntoLinesCursorAtHeadCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            lines = self.view.split_by_newlines(region)
            if len(lines) > 1:
                self.view.sel().clear()
                for line in lines:
                    begin, end = line.begin(), line.end()
                    self.view.sel().add(sublime.Region(end, begin))
