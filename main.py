import time, keyboard, os
import PySimpleGUI as sg
import mouse


def click(timer: int):
    while True:
        if keyboard.is_pressed(";"):
            print("pressed")
            break
        else:
            time.sleep(timer)
            mouse.click("left")


def startup():
    layout = [[sg.Text('Enter time interval :', size=(15, 1))],
              [sg.Input(default_text="10", key="timer", size=(15, 1), focus=True)],
              [sg.Button("Start"), sg.Button("Exit")]]
    window = sg.Window("Lostark anti-afk bot", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        if event == 'Start':
            window.Minimize()
            click(int(values['timer']))
        if event == 'Exit':
            break
    window.close()


if __name__ == '__main__':
    if os.name == "nt":
        startup()
    else:
        print("Your system isn't supported.")
