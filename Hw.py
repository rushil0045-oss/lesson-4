from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("Interest Calculator")

def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    Simple_interest = (p * r * t) / 100
    compound_interest = p * (1 + r / 100) ** t - p
    si.config(text=f"Simple Interest: {Simple_interest}")
    ci.config(text=f"Compound Interest: {compound_interest}: {compound_interest:.2f}")

principal_label = Label(window, text="Principal Amount:")
principal_label.pack()
rate_label = Label(window, text="Rate of Interest:")
rate_label.pack()
time_label = Label(window, text="Time (years):")
time_label.pack()

conform = Button(window, text="Calculate", command=calculate)
conform.pack()
principal_entry = Entry(window)
principal_entry.pack()
rate_entry = Entry(window)
rate_entry.pack()
time_entry = Entry(window)
time_entry.pack()

si = Label(window, text="")
si.pack()
ci = Label(window, text="")
ci.pack()

window.mainloop()
