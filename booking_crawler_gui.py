import PySimpleGUI as sg
import os

layout = [
      [sg.Text('Please select which data to scrape:')],
      [sg.Radio('Prices and availabilities', key = 'prezzi_disponibilita', group_id = 1, default=True, change_submits = True, enable_events=True)],
      [sg.Radio('Reviews and general descriptions', key = 'generali_recensioni', group_id = 1, default=False, change_submits = True, enable_events=True)],
      [sg.Text('checkin  ', key = 'text_1'), sg.Input(key='checkin', size=(20,1), disabled = True), sg.CalendarButton(button_text = 'choose date', key = 'cal_b_1', close_when_date_chosen=True, format = "%d-%m-%Y")],
      [sg.Text('checkout', key = 'text_2'), sg.Input(key='checkout', size=(20,1), disabled = True), sg.CalendarButton(button_text = 'choose date', key = 'cal_b_2', close_when_date_chosen=True, format = "%d-%m-%Y")],
      [sg.Button('Scrape websites!', key = 'scrape', size=(37,1), button_color=('blue', 'gray'))],
]

window = sg.Window('Booking crawler', layout, icon=r'.\booking_logo.ico')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'): break

# aggiorna la grafica in base ai radio button ==========================
    if event == 'prezzi_disponibilita':
        window['cal_b_1'].update(disabled = False)
        window['cal_b_2'].update(disabled = False)
        window['scrape'].update(disabled = False)
        window['text_1'].update(text_color = 'white')
        window['text_2'].update(text_color = 'white')
    
    if event == 'generali_recensioni':
        window['cal_b_1'].update(disabled = True)
        window['cal_b_2'].update(disabled = True)
        window['text_1'].update(text_color = 'gray')
        window['text_2'].update(text_color = 'gray')

# avvia il programma ====================================================
    if event == 'scrape':
        if values['prezzi_disponibilita'] == True:
            print("checkin: " + values['checkin'])
            print("checkout: " + values['checkout'])
            if not values['checkin'] and not values['checkout']: sg.popup_error('please insert checkin and checkout dates', no_titlebar = True, background_color = 'gray')
            else :
                os.system('cmd /c "ciao.py"')
                sg.popup('scraping availabilities and prices . . .')
                # inviare le date come parametro
                # inserire progress bar
    
        elif values['generali_recensioni'] == True:
            print("recensioni in arrivo zio")
            # lancia lo scraper dei dati generali e delle recensioni

        break

window.close()