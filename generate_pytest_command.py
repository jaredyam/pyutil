import sublime_plugin

from .osx_utils import call_terminal


class PytestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selected_regions = list(self.view.sel())
        filepath = self.view.file_name()
        if len(selected_regions) == 1 and not self.view.substr(selected_regions[0]):
            call_terminal(run_command='pytest {}'.format(filepath))
        else:
            for region in selected_regions:
                text = self.view.substr(region)
                command = 'pytest {}'.format(filepath) + ('::{}'.format(text)
                                                          if text else '')
                call_terminal(run_command=command)
