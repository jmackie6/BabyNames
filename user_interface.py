import tkinter as tk
import movie_name_study

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        # Create the option picker for the range of years
        self.range_selection = tk.StringVar(master)
        self.range_selection.set(0)
        self.select_range = tk.OptionMenu(master, self.range_selection, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.select_range.pack(side=tk.RIGHT)
        # Enter a Year
        self.year_entry = self.make_entry(master,"Year: ")#= tk.Entry(master)
        self.year_entry.pack()
        # Enter a baby name to investigate for this year
        self.name_entry = self.make_entry(master, "Name to graph (optional): ")#tk.Entry(master)
        self.name_entry.pack()
        # The quit button
        tk.Label(master, text="Year Span: ").pack(side=tk.RIGHT)
        self.button = tk.Button(frame, text='QUIT', fg='red', command=frame.quit)
        self.button.pack(side=tk.LEFT)
        # The run button
        print(self.year_entry.get(), self.range_selection.get())
        self.run_study = tk.Button(frame, text='Run', command= lambda: movie_name_study.MovieNameStudy
        (self.year_entry.get(), self.range_selection.get(), self.name_entry.get()))
        self.run_study.pack(side=tk.RIGHT)
    def make_entry(self, parent, caption, width=None, **options):
        tk.Label(parent, text=caption).pack(side=tk.LEFT)
        entry = tk.Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.LEFT)
        return entry



root = tk.Tk()

app = App(root)

root.mainloop()

root.destroy()