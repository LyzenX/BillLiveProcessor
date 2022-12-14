"""
origin niconvert
author muzuiget
"""
from blptk.tkmodules import tk, ttk, tku

class LoggingFrame(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='信息', padding=2)
        self.pack(fill=tk.BOTH, expand=True)
        self.grid_columnconfigure(1, weight=1)
        self.init_widgets()

    def init_widgets(self):
        scrolledtext = ttk.ScrolledText(self, width=64)
        scrolledtext.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrolledtext = scrolledtext
        tku.add_border_space(self, 1, 1)

    def get(self):
        return self.scrolledtext.get(1.0, 'end')

    def write(self, string):
        self.scrolledtext.config(state=tk.NORMAL)
        self.scrolledtext.insert('end', string)
        self.scrolledtext.see('end')
        self.scrolledtext.state = "disabled"
        self.scrolledtext.config(state=tk.DISABLED)

    def set(self, string):
        self.scrolledtext.config(state=tk.NORMAL)
        self.scrolledtext.delete("1.0", "end")
        self.write(string)
