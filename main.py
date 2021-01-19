#!/usr/bin/env python
from GUI import Application

if __name__ == '__main__':
    app = Application()
    app.master.resizable(width=False, height=False)
    app.master.title('Magic C')
    app.mainloop()
