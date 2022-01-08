import PySimpleGUI as sg                       
from Transposition import Encruption,Decription

# Define the window's contents
layout = [  [sg.Text("Put the Text ",auto_size_text = True)],     
            [sg.Input()],
            [sg.Text("Put the Key ")],
            [sg.Input()],
            [sg.Button('Encruption'),sg.Button('Decription')],
            [sg.Text("The Rusult is ")] ,
            [sg.Text(size=(40,1), background_color='white',text_color='Black',key='-OUTPUT-',auto_size_text = True)]
            ,[sg.Button('Quit')]]

# Create the window
window = sg.Window('Transposition Encription ', layout, resizable=True,finalize=True)      
                                                

# Do something with the information gathered
while(True):
    event, values = window.read()
    if (event == "Encruption"):
        Enc=Encruption(values[0],list(map(int,values[1].split())))
        window['-OUTPUT-'].update( Enc )

    elif (event == "Decription"):
        Dec=Decription(values[0],list(map(int,values[1].split())))
        window['-OUTPUT-'].update( Dec )
    else : break


window.close()                                  
