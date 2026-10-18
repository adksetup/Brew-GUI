from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel
from termcolor import cprint
import subprocess as subprcs

class BrewGui:
    def __init__(self, window: CTk):
        self.window = window
        self.window.geometry('300x300')
        self.window.resizable(False, False)
        self.window.wm_title('Brew GUI')
        self.home()
        
    def home(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.inst_btn: CTkButton = CTkButton(self.window, text='安装',
                                             command=self.inst, corner_radius=5)
        self.inst_btn.place(relx=0.5, rely=0.2, anchor='center')
        self.update_btn: CTkButton = CTkButton(self.window, text='更新',
                                               command=self.update, corner_radius=5)
        self.update_btn.place(relx=0.5, rely=0.4, anchor='center')
        self.uninst_btn: CTkButton = CTkButton(self.window, text='卸载',
                                               command=self.uninst, corner_radius=5)
        self.uninst_btn.place(relx=0.5, rely=0.6, anchor='center')  
        self.more_btn: CTkButton = CTkButton(self.window, text='更多',
                                             command=self.more, corner_radius=5)
        self.more_btn.place(relx=0.5, rely=0.8, anchor='center')     
        
    def inst(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            home_btn1: CTkButton = CTkButton(self.window, text='返回主界面',
                                             command=self.home, corner_radius=5)
            home_btn1.place(relx=0.1, rely=0.1, anchor='center')
            inst_label: CTkLabel = CTkLabel(self.window, text='安装',
                                            font=('Helvetica bold', 26))
            inst_label.place(relx=0.5, rely=0.4, anchor='center')
            self.app_entry1: CTkEntry = CTkEntry(self.window, width=200, placeholder_text='请输入要安装的应用',
                                                 corner_radius=5)
            self.app_entry1.place(relx=0.5, rely=0.6, anchor='center')
            inst_btn: CTkButton = CTkButton(self.window, text='安装',
                                              command=self.inst_func, corner_radius=5)
            inst_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e1:
            cprint('Error: {0}'.format(e1), 'red')
            
    def update(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            home_btn2: CTkButton = CTkButton(self.window, text='返回主界面',
                                             command=self.home, corner_radius=5)
            home_btn2.place(relx=0.1, rely=0.1, anchor='center')
            update_label: CTkLabel = CTkLabel(self.window, text='更新',
                                              font=('Helvetica bold', 26))
            update_label.place(relx=0.5, rely=0.4, anchor='center')
            self.app_entry2: CTkEntry = CTkEntry(self.window, width=200, placeholder_text='请输入要更新的应用',
                                            corner_radius=5)
            self.app_entry2.place(relx=0.5, rely=0.6, anchor='center')
            update_btn: CTkButton = CTkButton(self.window, text='更新',
                                              command=self.update_func, corner_radius=5)
            update_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e2:
            cprint('Error: {0}'.format(e2), 'red')
        
    def uninst(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            home_btn3: CTkButton = CTkButton(self.window, text='返回主界面',
                                             command=self.home, corner_radius=5)
            home_btn3.place(relx=0.1, rely=0.1, anchor='center')
            uninst_label: CTkLabel = CTkLabel(self.window, text='卸载',
                                              font=('Helvetica bold', 26))
            uninst_label.place(relx=0.5, rely=0.4, anchor='center')
            self.app_entry3: CTkEntry = CTkEntry(self.window, width=200, placeholder_text='请输入要卸载的应用',
                                            corner_radius=5)
            self.app_entry3.place(relx=0.5, rely=0.6, anchor='center')
            uninst_btn: CTkButton = CTkButton(self.window, text='卸载',
                                              command=self.uninst_func, corner_radius=5)
            uninst_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e3:
            cprint('Error: {0}'.format(e3), 'red')
        
    def more(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            home_btn4: CTkButton = CTkButton(self.window, text='返回主界面',
                                             command=self.home, corner_radius=5)
            home_btn4.place(relx=0.1, rely=0.1, anchor='center')
            more_label: CTkLabel = CTkLabel(self.window, text='更多',
                                            font=('Helvetica bold', 26))
            more_label.place(relx=0.5, rely=0.4, anchor='center')
            update_brew_btn: CTkButton = CTkButton(self.window, text='更新Brew',
                                                   command=self.update_brew, corner_radius=5)
            update_brew_btn.place(relx=0.5, rely=0.6, anchor='center')
            app_list_btn: CTkButton = CTkButton(self.window, text='应用列表',
                                                command=self.app_list, corner_radius=5)
            app_list_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e4:
            cprint('Error: {0}'.format(e4), 'red')
            
    def update_brew(self):
        try:
            subprcs.run('brew update', shell=True)
            cprint('Brew 已完成更新', 'green')
        except Exception as e5:
            cprint('Error: {0}'.format(e5), 'red')
        
    def app_list(self):
        try:
            subprcs.run('brew list', shell=True)
        except Exception as e6:
            cprint('Error: {0}'.format(e6), 'red')
        
    def inst_func(self):
        try:
            subprcs.run('brew install {0}'.format(self.app_entry1.get()), shell=True)
            cprint('{0} 已安装完成'.format(self.app_entry1.get()), 'green')
        except Exception as e7:
            cprint('Error: {0}'.format(e7), 'red')
        
    def uninst_func(self):
        try:
            subprcs.run('brew uninstall {0}'.format(self.app_entry3.get()), shell=True)
            cprint('{0} 已卸载完成'.format(self.app_entry3.get()), 'green')
        except Exception as e8:
            cprint('Error: {0}'.format(e8), 'red')
        
    def update_func(self):
        try:
            subprcs.run('brew upgrade {0}'.format(self.app_entry2.get()), shell=True)
            cprint('{0} 已完成更新'.format(self.app_entry2.get()), 'green')
        except Exception as e9:
            cprint('Error: {0}'.format(e9), 'red')

if __name__ == '__main__':
    app = CTk()
    gui = BrewGui(app)
    app.mainloop()