import sublime
import sublime_plugin


class SplitIntoLinesCursorAtHeadCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        new_region_of_lines = []
        for region in self.view.sel():
            lines = self.view.split_by_newlines(region)
            self.view.sel().clear()

            for line in lines:
                indent = 0
                for c in self.view.substr(line):
                    if c == ' ':
                        indent += 1
                    else:
                        break

                new_region_of_lines.append((line.end(), line.begin() + indent))

        for region in new_region_of_lines:
            self.view.sel().add(sublime.Region(*region))
