import sublime_plugin

import os


class CreateNewFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel(
            'New File', '', self.on_done, None, None)

    def on_done(self, new_filename):
        filepath = self.window.active_view().file_name()
        new_filepath = os.path.join(os.path.dirname(filepath),
                                    new_filename)
        new_filepath = new_filepath.replace(' ', '\\ ')
        os.system('subl {}'.format(new_filepath))
