ttk::frame .frm -padding 10
grid .frm
grid [ttk::label .frm.lbl -text "Hello World!"] -column 0 -row 0
grid [ttk::button .frm.btn -text "Quit" -command "destroy ."] -column 1 -row 0
btn = ttk.Button(frm, ...)
print(btn.configure().keys())
print(set(btn.configure().keys()) - set(frm.configure().keys()))
print(dir(btn))
print(set(dir(btn)) - set(dir(frm)))
