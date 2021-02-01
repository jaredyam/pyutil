import sublime_plugin

import os


class OpenNewTerminalTabCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filepath = os.path.dirname(self.view.file_name())
        new_tab_command = """osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' -e 'tell application "Terminal" to do script "cd {}" in selected tab of the front window'""".format(
            filepath)

        os.system(new_tab_command)


class OpenNewTerminalWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filepath = os.path.dirname(self.view.file_name())
        new_window_command = ('open -a /System/Applications/'
                              'Utilities/Terminal.app {}'.format(filepath))
        os.system(new_window_command)
