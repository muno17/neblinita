import PySimpleGUI as sg


layout = [[sg.Text('neblina', font='Monaco'), sg.Text('', key='-OUTPUT-')],
          [sg.Combo(('input1', 'input2', 'input3')), sg.Combo(('output1', 'output2', 'output3'))],
          [sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco'),
           sg.Slider((0,100), key='-SLIDER-', orientation='v', tick_interval=50, enable_events=True, disable_number_display=True, font='Monaco')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('neblina', layout)

while True:             # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #window['-LEFT-'].update(int(values['-SLIDER-']))
    #window['-RIGHT-'].update(int(values['-SLIDER-']))
    if event == 'Show':
        sg.popup(f'The slider value = {values["-SLIDER-"]}')
window.close()