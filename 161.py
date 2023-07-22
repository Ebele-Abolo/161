from tkinter import filedialog
name = ""
my_text.delete(1.0, END)
input_file_name.delete(0, END)
html_file = filedialog.askopenfilename(title=" Open html File", filetypes=(("html Files", "*html"),))
name = os.pth.basename(html_file)
formated_name = name.split('.')[0]
input_file_name.insert(END, formated_name)
html_file = open(name, 'r')
paragraph = html_file.read()