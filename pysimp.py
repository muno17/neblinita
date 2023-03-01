import PySimpleGUI as sg

layout = [[sg.Text('neblina'), sg.Text('', key='-OUTPUT-')],
          [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('wet/dry'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('melt'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('fractals'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('luz delay'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('luz space'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('haze'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('sombra delay'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
           [sg.Text('sombra space'), sg.Text('', key='-OUTPUT-')],
           [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('neblina', layout)

while True:             # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window['-LEFT-'].update(int(values['-SLIDER-']))
    window['-RIGHT-'].update(int(values['-SLIDER-']))
    if event == 'Show':
        sg.popup(f'The slider value = {values["-SLIDER-"]}')
window.close()