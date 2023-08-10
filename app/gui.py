import PySimpleGUI as sg


class Gui:
    sg.theme('BluePurple')

    def input_window(self, window_title, window_text):
        layout = [[sg.Text(window_text), sg.Text(size=(15, 1), key='-OUTPUT-')],
                  [sg.Input(key='-IN-', focus=True, enable_events=True)],
                  [sg.Button('Подтвердить'), sg.Button('Выход')]]

        window = sg.Window(window_title, layout, grab_anywhere=True)

        while True:
            self.event, self.values = window.read()
            print(self.event, self.values)
            #if self.event == sg.WIN_CLOSED or self.event == 'Выход' or self.event = "-ESCAPE-":
            if self.event in (sg.WIN_CLOSED, 'Выход'):
                break
            """if self.event == 'Подтвердить':
                # Update the "output" text element to be the value of "input" element
                #window['-OUTPUT-'].update(self.values['-IN-'])
                window.close()
                return self.values['-IN-']"""

            if self.event in ('Подтвердить'):
                window.close()
                return self.values['-IN-']

    def show_message_window(self, window_title, window_text, size=(20, 10)):
        layout = [[sg.Text(window_text, size=(size[0], size[1])), sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Button('Подтвердить')]]

        window = sg.Window(window_title, layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Подтвердить':
                window.close()
                break

        window.close()

    def pop_up(self):
        sg.popup('Значение должно быть числом!')


