import sublime
import sublime_plugin

import os


class CreateNewFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        assert self.view.file_name() is not None, sublime.error_message(
            'expected at least a base view/file opened')

        filename_selections = [self.view.substr(region)
                               for region in self.view.sel()
                               if self.view.substr(region)]

        if filename_selections:
            for filename in filename_selections:
                self.create_new_file(filename)
        else:
            self.view.window().show_input_panel('Create New File', '.py',
                                                self.on_done,
                                                None,
                                                None)

    def on_done(self, filename):
        self.create_new_file(filename)

    def create_new_file(self, filename):
        filepath = os.path.join(os.path.dirname(self.view.file_name()),
                                filename)
        filepath = filepath.replace(' ', '\\ ')
        os.system('subl {}'.format(filepath))
