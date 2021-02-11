import sublime_plugin

from .osx_utils import call_terminal, osx_only


class RunPytestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        osx_only()
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


class RunFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filepath = self.view.file_name()
        call_terminal(run_command='python {}'.format(filepath))
