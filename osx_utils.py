import os


def call_terminal(run_command=None, new_tab=False):
    call_terminal = """osascript -e 'tell application "Terminal" to activate' """
    if new_tab:
        call_terminal += ("""-e 'tell application "System Events" """
                          """to tell process "Terminal" """
                          """to keystroke "t" using command down' """)
    if run_command:
        call_terminal += ("""-e 'tell application "Terminal" """
                          """to do script "{}" """
                          """in selected tab of the front window' """.format(run_command))

    os.system(call_terminal)


def open_terminal_with_new_window(init_path=None):
    init_path = init_path if init_path is not None else '~'
    os.system('open -a /System/Applications/'
              'Utilities/Terminal.app {}'.format(init_path))
