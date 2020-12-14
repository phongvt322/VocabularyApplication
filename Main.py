import PySimpleGUI as sg
import pickle
import random
import time
import os

"""
  DESIGN PATTERN 2 - Multi-read window. Reads and updates fields in a window
"""
print("123")
sg.theme('Dark Amber')    # Add some color for fun

# 1- the layout
layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Multiline(size=(100,30), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True, auto_refresh=True)#,
                # sg.Frame('Labelled Group',[[sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
                #                         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
                #                         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10)]]
                #                         )
                                        ],
          [sg.Text('User:', size=(15,1)), sg.Input(key='-USER-',default_text='phongvo')],
          [sg.Text('Number of Word:', size=(15,1)), sg.Input(key='-NWORD-')],
          [sg.Button('Show'), sg.Button('Exit') ],
          [sg.Text('Delay:', size=(15,1)), sg.Input(key='-DELAY-',default_text='2')],
          [sg.Button('Generate Voice file'), sg.Button('Read')]]


# 2 - the window
window = sg.Window('Học Từ Vựng', layout)

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':

        valid_user = ['phongvo']
        if values['-USER-'] not in valid_user:
            window['-OUTPUT-'].update("Crack à bạn ơi?")
        else:
            if values['-NWORD-'] == '':
                values['-NWORD-'] = 100

            with open('Resource/index_dict.pkl', 'rb') as f:
                dict_index_tmp =  pickle.load(f)

                dict_index = {}
                for k1 in random.sample( list( dict_index_tmp.keys() ) , int(values['-NWORD-']) ):
                    dict_index[k1] = dict_index_tmp[k1]
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-USER-'])

            sg.cprint(f'Data from the thread ', colors='white on purple', end='')
            sg.cprint("1", colors='white on purple', end='\n')
            with open("Resource/anhviet109K.txt") as dict_file:
                # for k2 in dict_index.keys():
                dict_index_ = [dict_index[k2][0] for k2 in dict_index.keys()]
                # sg.cprint(dict_index, colors='red on white', end='')
                # word_index = dict_file.readlines()[dict_index]
                for i, line in enumerate(dict_file):
                    if i in dict_index_:
                        sg.cprint(line, colors='red on white', end=': ',)
                    if i - 1 in dict_index_:
                        sg.cprint(line, colors='grey on white', end='',)
                    if i - 2 in dict_index_:
                        sg.cprint(line, colors='red on white', end='\n',)

            # Log Word generated
            timestamp = int(time.time())
            log_file_tmp = str(timestamp) + values['-USER-']
            f = open("log/" + log_file_tmp, "w")
            f.write('\n'.join(dict_index.keys()))
            f.close()

            f_log = open("log/" + "last_log", "w")
            f_log.write(log_file_tmp)
            f_log.close()
            # for k2 in dict_index.keys():
            #     sg.cprint(k2, colors='red on white', end='',)
            #     sg.cprint(dict_index[k2], colors='black on white', end='\n',)
            #     sg.cprint(dict_index[k2][1], colors='black on white', end='\n',)
            # In older code you'll find it written using FindElement or Element
            # window.FindElement('-OUTPUT-').Update(values['-IN-'])
            # A shortened version of this update can be written without the ".Update"
            # window['-OUTPUT-'](values['-IN-'])
    if event == 'Read':
        with open("log/" + "last_log") as last_log_tmp:
            last_log_file = ''.join(last_log_tmp.readlines())
            with open("log/" + last_log_file) as last_log:
                for i, line in enumerate(last_log):
                    # window['-ML-'].print(line, text_color='black', background_color='white', auto_refresh=True)
                    sg.cprint(line, colors='red on white', end='\n')
                    time.sleep(int(values['-DELAY-']))
                    # time.sleep(0.5)
                    os.system("gtts-cli " + line.replace('\n','') + " | play -t mp3 -")
# 4 - the close
window.close()
