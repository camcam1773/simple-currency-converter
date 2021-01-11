import tkinter as tk
import exchange_rate as er


def close():
    exit(0)


def change_dropdown1(*args):
    print(dropdown_text1.get())


def change_dropdown2(*args):
    print(dropdown_text2.get())


def button_ok_action():
    from_currency = dropdown_text1.get()
    to_currency = dropdown_text2.get()
    amount = field1.get()
    if amount == '':
        return
    try:
        amount = float(amount)
    except ValueError:
        result.set('NaN')
        return
    rate: float = er.get_all_for_base(from_currency)['rates'].get(to_currency, 1)
    converted = amount * rate
    result.set(round(converted, 2))


def key_enter_action(event):
    button_ok_action()


root = tk.Tk()
root.title('CC')
root.option_add('*Font', '72')

root.resizable(False, False)
label1 = tk.Label(root, text='Currency Converter')
field1 = tk.Entry(root, width=10)
button_ok = tk.Button(root, text='OK', command=button_ok_action)
button_exit = tk.Button(root, text='Close', command=close)
dropdown_text1 = tk.StringVar(root)
dropdown_text2 = tk.StringVar(root)
result = tk.StringVar(root)
label_result = tk.Label(root, textvariable=result)

codes = er.Currency.codes
dropdown_text1.set('USD')
dropdown1 = tk.OptionMenu(root, dropdown_text1, *codes)
dropdown_text2.set('EUR')
dropdown2 = tk.OptionMenu(root, dropdown_text2, *codes)

label1.grid(row=0, padx=5)
dropdown1.grid(row=1, column=0)
dropdown2.grid(row=1, column=1)
field1.grid(row=2, column=0, padx=1, pady=1)
label_result.grid(row=2, column=1, padx=1, pady=1)
button_ok.grid(row=3, column=0)
button_exit.grid(row=3, column=1)
root.bind('<Return>', key_enter_action)
root.geometry('250x130')

root.mainloop()
