import PySimpleGUI as sg
import athema 

sg.theme('Athema')

quotes = [] # will contain [a list of] "quote" dictionary 
def layoutMethod(): 
    return [[sg.Text(text="Source = first input box", size=(30,2), auto_size_text=True)],
            [sg.Input(key='source-input')], [sg.Input(key='quote-input')],
            *[[sg.Text(text="Quote: " + quotes[_quote]["source"], size=(30,2), auto_size_text=True), [sg.Text(text="Source: " + quotes[_quote]["quote"], size=(30,2), auto_size_text=True),]] for _quote in range(len(quotes))],
            [sg.Button('Add quote'), sg.Button('Close')]]

layout = layoutMethod()

location = (300, 300)
window = sg.Window('Quotes', location=location).Layout(layout)
def main(window):
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': 
        window.close()
        return 
    if event == "Add quote":
        quoteDict = {
            "source": values["source-input"], 
            "quote": values["quote-input"]
        } 
        quotes.append(quoteDict)
        layout = layoutMethod()
        location = window.CurrentLocation() 
        newWindow = sg.Window('Quotes', location=location).Layout(layout)
        window.Close()
        window = newWindow
    main(window)
main(window) 

