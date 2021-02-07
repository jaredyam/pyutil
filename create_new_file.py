import sublime_plugin

import os


class CreateNewFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.viewpath = self.view.file_name()
        selected_filenames = [self.view.substr(region)
                              for region in self.view.sel()
                              if self.view.substr(region)]
        if selected_filenames:
            for new_filename in selected_filenames:
                self.create_new_file(new_filename)
        else:
            self.view.window().show_input_panel('New File', '',
                                                self.on_done,
                                                None,
                                                None)

    def on_done(self, new_filename):
        self.create_new_file(new_filename)

    def create_new_file(self, new_filename):
        new_filepath = os.path.join(os.path.dirname(self.viewpath),
                                    new_filename)
        new_filepath = new_filepath.replace(' ', '\\ ')
        os.system('subl {}'.format(new_filepath))
