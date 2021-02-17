import sublime_plugin

from .osx_utils import call_terminal, osx_only


class RunPytestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        osx_only()
        selections = self.view.sel()
        filepath = self.view.file_name()
        _cd_to_current_dir(filepath)
        if len(selections) == 1 and not self.view.substr(selections[0]):
            call_terminal(run_command='pytest -s {}'.format(filepath))
        else:
            for region in selections:
                text = self.view.substr(region)
                if not text:
                    continue
                command = 'pytest -s {}'.format(filepath) + '::{}'.format(text)
                call_terminal(run_command=command)


class RunFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filepath = self.view.file_name()
        _cd_to_current_dir(filepath)
        call_terminal(run_command='python {}'.format(filepath))


def _cd_to_current_dir(filepath):
    parentdir = '/'.join(filepath.split('/')[:-1])
    call_terminal(run_command='cd {}'.format(parentdir))
