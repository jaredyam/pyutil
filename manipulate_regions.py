import sublime_plugin


class SplitRegionIntoLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            lines = self.view.split_by_newlines(region)
            if len(lines) > 1:
                self.view.sel().clear()
                for line in lines:
                    self.view.sel().add(line)
