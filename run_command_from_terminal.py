class RunFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        call_terminal(run_command='python {}'.format(filepath))
