#importing all modules neccesary to carry out functions
import os
os.environ['KIVY_IMAGE'] = 'pil, sdl2'
from kivy.config import Config
Config.set('postproc','desktop','1')
Config.set('kivy','exit_on_escape','1')
Config.set('kivy','log_enable','1')
Config.set('kivy', 'log_maxfiles', '-1')
Config.set('widgets', 'scroll_friction','float')
Config.set('widgets', 'scroll_distance', '4')
Config.set('graphics','borderless','0')
Config.set('graphics','rotation','0')
Config.set('graphics','full_screen','1')
Config.set('graphics','allow_screensaver','1')
Config.set('graphics','kivy_clock','free_all')
from kivy.core.window import Window
Window.clearcolor=(0,0,0,0)
from kivy.core.window import Window
from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.core.audio import Sound
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.checkbox import CheckBox
from kivy.uix.stencilview import StencilView
from kivy.core.image import Image
from kivy.uix.switch import Switch
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.listview import ListItemButton,ListItemLabel
from kivy.properties import StringProperty,NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.graphics import Color,Rectangle, Line
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.popup import Popup
import os
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionBar,ActionView,ActionGroup,ActionButton,ActionPrevious, ActionView,ActionOverflow, ContextualActionView
from kivy.uix.settings import SettingsWithSidebar
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.utils import platform as core_platform
from functools import partial
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.audio import SoundLoader
Clock.max_iteration=40
import pygame, time
import io 
import mysql
#loading the Masenoeasy.kv file
Builder.load_file('Masenoeasy.kv')
#Root class binded to updated 


class Rootwidget(GridLayout):
    def __init__(self, *args):
        super(Rootwidget, self). __init__(*args)
        manager = ObjectProperty(None)
        self.bind(size=self.update_rec, pos=self.update_rec)
        self.rec =Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos =self.pos



#class for adding photo and continue with registartion
class Helpwidget(GridLayout):
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Helpwidget, self). __init__(**kwargs)
        with self.canvas.before:
            Color(1,1,1,0)
    #OPENNIGN HELP FILE
    def opentext(self, *args):
        f = open('CV.text', 'r')
        return f



class Content2(GridLayout):
    def __init__(self, **kwargs):
        super(Content2, self). __init__(**kwargs)
        self.cols=1
        self.but = Button(text='Add_photo',font_size=24)
        self.but2 = Button(text='continue......................', font_size=12)
        for self.buts in [self.but, self.but2]:
            self.add_widget(self.buts)




#class for changing number
class Changing(GridLayout):
    def __init__(self, **kwargs):
        super(Changing, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            self.rec = Rectangle(size=self.size, pos=self.pos, source='icons/maseno4.png')
        self.cols=2
        self.label=Label(text='Previous_Number', font_size=15)
        self.n_label=TextInput(multline=False)
        self.label2 = Label(text='Current_Number', font_size=15)
        self.n_label2=TextInput(multline=False)
        self.next = Button(text='NEXT', font_size=20,background_color=[1,1,1,0],on_press=self.change_numbers)
        for widgets in [self.label, self.n_label, self.label2, self.n_label2, self.next]:
            self.add_widget(widgets)   
    def update_rec(self, *args):
        self.rec.size = self.size
        self.rec.pos = self.pos
    def change_numbers(self, *args):
        print('dswerwrgr')

#my banking statements
class Bank(StackLayout):
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Bank, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            self.rec = Rectangle(size=self.size, pos=self.pos, source='icons/watch.jpg')
        self.label = Label(text='crypt pin',bold=True, size_hint=(.1, .1))
        self.text = TextInput(multline=False,password=True,size_hint=(.4,.1), pos_hint={'top': 1})
        self.button = Button(text='Ok', size_hint=(.2,.1), on_press=self.press, background_color=[1,0,0,1])
        for data in [self.label,self.text,self.button]:
            self.add_widget(data)
    def press(self, *args):
        if str(self.text.text):
            for acces in [self.label,self.text, self.button]:
                self.remove_widget(acces)
            self.button2 = Button(text='logout', size_hint=(.1, .1))
            for bts in [self.button2]:
                self.add_widget(bts)
        else:
            p = Popup(title='error', size_hint=(.2,.2), content=Label(text='incorrect pin'))
            p.open()
    

    def update_rec(self, *args):
        self.rec.size = self.size
        self.rec.pos = self.pos

        
#class for documents
class Books(StackLayout):
    def __init__(self, **kwargs):
        super(Books, self). __init__(**kwargs)
        self.cols=2
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            self.rec = Rectangle(size=self.size, pos=self.pos, source='icons/library.jpg')
        self.but = Button(text='Upload',background_color=[1,1,1,0], size_hint=(.2, .1), pos_hint={'top': 1})
        self.but2 = Button(text='Delete',background_color=[1,1,1,0], size_hint=(.2, .1), pos_hint={'top': 1})
        for btns in [self.but, self.but2]:
            self.add_widget(btns)
    def update_rec(self, *args):
        self.rec.size = self.size
        self.rec.pos = self.pos


#class of menu
class Menuscreen(GridLayout):
    def __init__(self, **kwargs):
        super(Menuscreen, self). __init__(**kwargs)
    def mybanks(self, *args):
        banks = Bank(cancel=self.dismiss)
        self._banks = Popup(title='Banking Statements', title_align='center', size_hint=(1, 1), content=banks)
        self._banks.open()


    def dismiss(self, *args):
        self._banks.dismiss()
    def books(self, *args):
        con = Books()
        self._con = Popup(title='My Library', title_align='center', content=con)
        self._con.open()
        









#classs for searching
class Search(GridLayout):
    cancel = ObjectProperty(None)
    textinputs = ObjectProperty(None)
    displaycontents = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Search, self). __init__(**kwargs)
        self.cols=1
        with self.canvas.before:
            Color(1,0,1,1)

        
#class for  profile
class Myprofile(GridLayout):
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Myprofile, self). __init__(**kwargs)
        with self.canvas.before:
            Color(1,0,0,1)
#adding profile photo to the second widget
    def add_photo(self, *args):
        photo = Photo(save=self.save, cancel=self.dismiss_photo)
        self._photo = Popup(title='photo', title_align='center', size_hint=(.5, .5), content=photo)
        self._photo.open()
    def dismiss_photo(self, *args):
        self._photo.dismiss()
    def active(self, *args):
        screen_manager = ScreenManagement()
        screen_manager.current='active'


#adding my ststus
    def mystatus(self, *args):
        status = Mystatus(post=self.poststatus,cancel=self.statuscancel)
        self._status = Popup(title='my status', content=status)
        self._status.open()
    def statuscancel(self, *args):
        self._status.dismiss()



#saving myphoto
    def save(self, path, filename):
        with open(os.path.join(path, filename[0])) as photo:
            self._image = Image(source='photo')
            self.previouswidget.add_widget(ActionButton(icon='self._image'))
        self.dismiss_photo()




#class containing all inputs to regiser

class account(GridLayout):
    def __init__(self, **kwargs):
        cancel = ObjectProperty(None)
        super(account, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,1)
            self.rec=Rectangle(size=self.size, pos=self.pos ,source='icons/maseno8.png')
        self.cols=2
        self.username = Label(text='Username',font_size=15, size_hint=(1,1), pos_hint={'top': 1})
        self.add_widget(self.username)
        self.n_username = TextInput(multline=False,  size_hint=(1,.5),pos_hint={'top': .9})
        self.add_widget(self.n_username)
        self.email = Label(text='Email', font_size=15, size_hint=(1,1),pos_hint={'top': .8})
        self.add_widget(self.email)
        self.n_email=TextInput(multline=False, size_hint=(1, 1),pos_hint={'top': .8})
        self.add_widget(self.n_email)
        self.phone = Label(text='Phone_Number', font_size=15, size_hint=(1, 1), pos_hint={'top': .7})
        self.add_widget(self.phone)
        self.n_phone = TextInput(multline=False, size_hint=(1, 1), pos_hint={'top': .6})
        self.add_widget(self.n_phone)
        self.password = Label(text='crypt pin',font_size=15, size_hint=(1, 1), pos_hint={'top': .5})
        self.add_widget(self.password)
        self.n_password = TextInput(multline=False, password=True,  size_hint=(1 ,1), pos_hint={'top': .4})
        self.add_widget(self.n_password)
        Register = Button(text='Register',text_color=[1,0,1,1] ,font_size=12,background_color=[1,1,1,1], on_press=self.login, size_hint=(1, .3))
        self.add_widget(Register)
        number = Button(text='Change Number',text_color=[1,0,1,1], font_size=14,background_color=[1,1,1,1], on_press=self.change_number, size_hint=(1, .3))
        self.add_widget(number)
    def update_rec(self, *args):
        self.rec.size = self.size
        self.rec.pos = self.pos

#function for capturing deatils
    def login(self, *args):
        from kivy.storage.jsonstore import JsonStore
        import mysql
        connection = mysql.connect('127.0.0.1', '8080', password='Goodper3son;;', db='accounts',username='elvis')
        con = connection.execute()
        store = JsonStore('account.json')
        if str(self.n_username.text) and str(self.n_email.text) and str(self.n_phone) and str(self.n_password):
            store.put('credentilas', user=self.n_username.text, email=self.n_email.text, phone=self.n_phone.text, password=self.n_password.text)
            if True:
                co = VideoPlayer(source='video/video2.avi', state='play', volume=1)
                q = Popup(title='details',title_align='center', content=co, size_hint=(1, 1))
                q.open()
                Clock.schedule_once(q.dismiss,40)
                
        else:
            co =Label(text='retry')
            e =Popup(title='error will uploading check your details',title_color=[1,0,1,1] ,content=co, size_hint=(.2, .2)).open()
            Clock.schedule_once(e.dismiss, .90)

#function for changing number
    def change_number(self, *args):
        content3 = Changing()
        pop3 = Popup(title='SHIFT',title_size=24,title_color=[1,0,1,1], content=content3, size_hint=(.7, .7))
        pop3.open()




class videofiles(GridLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(videofiles, self). __init__(**kwargs)
        self.cols =2
        self.secondlabel = Label(text='first video chat',size_hint=(.4, .4), pos_hint={'top': 1})
        self.secondlabel.bind(on_press=self.secondlabel)
        self.textinput = TextInput(size_hint=(.2, .2), pos_hint=(.3, .4))



#class for adding photo
class Photo(FloatLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)



#musictoggle for music class
class Musictoggle(GridLayout):
    loading= ObjectProperty(None)
    canceling = ObjectProperty(None)


#widget for mystatus
class Mystatus(FloatLayout):
    cancel = ObjectProperty(None)
    post = ObjectProperty(None)
    textinput = ObjectProperty(None)


#class for a child of the parent
class Floating(FloatLayout):
    videowidget = ObjectProperty(None)
    musicwidget = ObjectProperty(None)
    registerwidget = ObjectProperty(None)
    profilesecond = ObjectProperty(None)
    myprofile = ObjectProperty(None)
    settings =ObjectProperty(None)
    helpwidget = ObjectProperty(None)
    actionBar = ObjectProperty(None)
    previouswidget = ObjectProperty(None)
    textInput = ObjectProperty(None)
#function for adding widget
    def __init__(self, **kwargs):
        super(Floating, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec =Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos =self.pos
#search toggle to search for objects
    def search(self, *args):
        contents = Search(cancel=self.dismisssearch)
        self._search = Popup(title='search', title_align='center', content=contents,size_hint=(.8, 1), pos_hint={'top': 1})
        self._search.open()
    def dismisssearch(self, *args):
        self._search.dismiss()
#cancelling the popup to add photo
    def dis(self, *args):
        self._photo.dismiss()
#cloasing music popup
    def musicdiss(self, *args):
        self._muisc.dismiss()
#adding photo on second action previous bar
    def adding_photo(self, *args):
        photocon = Photo(load=self.save, cancel=self.dis)
        self._photo = Popup(title='add_photo', title_align='center', content=photocon, size_hint=(.5, .5))
        self._photo.open()
#opening music popup
    def musicloader(self, *args):
        musictoggle = Musictoggle(loading=self.loading, canceling=self.musicdiss)
        self._music = Popup(title='Music Loader', title_align='center',size_hint=(.5, .5), content=musictoggle)
        self._music.open()

#function for laoding music files
    def loading(self, path, filename):
        with open(os.path.join(path, filename[0])) as music:
            self.sound = Sound.load('music')
            return self.sound.play()
            self.textinput.text=music
        self.musicdiss()
#playing nextsong
    def nextsong(self, *args):
        for audio in music:
            audio = +1
            sound=SoundLoader('audios')
            sound.play()
            self.musicinput.clear()
            self.musicinput.text=self.f
#playing music when pressing play button
    def playbutton(self, *args):
            sound = Sound.load('self.f')
            sound.play()
            self.musicinput.clear()
            self.musicinput.text=self.f
#playing previous song
    def previoussonng(self, *args):
        for self.f in music:
            self.f=-1
            sound = SoundLoader(self.f)
            sound.play()
            self.musicinput.clear()
            self.musicinput.text=self.f
#stoping the music from playing
    def stopmusic(self, *args):
        sound.stop()

#adding menu functions
    def menu(self, *args):
        menuscreen = Menuscreen(cancel=self.cancelmenu)
        self._menu = Popup(title='Menu', title_align='center', content=menuscreen, size_hint=(.3, .6))
        self._menu.open()    
    def cancelmenu(self, *args):
        self._menu.dismiss()  

    def poststatus(self, *args):
        for data in self.textinput.text:
            data.open()

#help settings
    def help(self, *args):
        helpwidget = Helpwidget(cancel=self.cancelhelp)
        self._help = Popup(title='search help', title_align='center', content=helpwidget, size_hint=(.2,.4))
        self._help.open()
    def cancelhelp(self, *args):
        self._help.dismiss()





#my profile
    def profilecancel(self, *args):
        self._myprofile.dismiss()
    def myprofile(self, *args):
        myprofile = Myprofile(cancel=self.profilecancel)
        self._myprofile = Popup(title='profile', title_align='center', content=myprofile, size_hint=(.3, .7))
        self._myprofile.open()



#function for registering
    def createaccount(self, *args):
        time=80
        content = account(cancel=self.dismissregis)
        self._pop=Popup(title=' Register', title_font='Roboto', title_align='center',title_color=[1,0,1,1], content=content, size_hint=(.7,.7))
        self._pop.open()
        if True:
            Clock.schedule_once(self._pop.dismiss, time)
#dismissing register toggle
    def dismissregis(self, *args):
        self._pop.dismiss()
#closing the video popup
    def dismiss(self, *args):
        self._popvida.dismiss()
#function for adding photo
    def addvideo(self, *args):
        contentv=videofiles(load=self.load, cancel=self.dismiss)
        self._popvida = Popup(title='Videos', title_font='Roboto', title_align='center', content=contentv, size_hint=(.5,.5))
        self._popvida.open()
#loading a video
    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            video = 'stream.avi'
            w = VideoPlayer(source='video',volume=1, state='play', size_hint=(1, 1), pos_hint={'top': 1}, background_color=[1,1,1,0], options={'allow_stretch':'True'})
            self.videowidget.add_widget(w)
        self.dismiss()
#class for managing screens

class ScreenManagement(ScreenManager):
    activityScreen = ObjectProperty(None)
    publicScreen = ObjectProperty(None)
    notificationScreen = ObjectProperty(None)
    chatScreen = ObjectProperty(None)
    callsScreen = ObjectProperty(None)
    freindsScreen=ObjectProperty(None)
    myaccountScreen = ObjectProperty(None)
    mydocsScreen = ObjectProperty(None)
    mysecretsScreen = ObjectProperty(None)
    myscreenbutton = ObjectProperty(None)

#classes for  screens
class Activity(Screen):
    pass

#class for public status
class Publicstatus(Screen):
    pass



#class for notifications
class Notifications(Screen):
    pass



#class for calls
class Calls(Screen):
    pass


#class for freinds
class Freinds(Screen):
    pass


#class for chating
class Chats(Screen):
    pass


#class for bank account
class Myaccount(Screen):
    pass


#class for important documents
class Mydocs(Screen):
    pass


#class for uploading importing secrets
class Mysecrets(Screen):
    pass


#class for screen buttons to be switched
class Screenbuttons(GridLayout):
    activebutton = ObjectProperty(None)
    publicScreen = ObjectProperty(None)
    chat = ObjectProperty(None)
    notification = ObjectProperty(None)
    call = ObjectProperty(None)
    account = ObjectProperty(None)
    documents = ObjectProperty(None)
    my_secrets = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Screenbuttons, self). __init__(**kwargs)
        self.cols=1
    def publicstatus(self, *args):
        screen_manager = ScreenManagement()
        screen_manager.current = 'public_status'
    def chat(self, *args):
        screen_manager = ScreenManagement()
        screen_manager.current = 'chats'
    def notifications(self, *args):
        screen_manager = ScreenManagement()
        screen_manager.current = 'notifications'
    def calls(self, *args):
        screen_manager = ScreenManagement()
        screen_manager.current = 'call'


#Main class
class MasenoeasyApp(App):
    def build(self):
        root = Rootwidget()
        sm = ScreenManagement(transition=SwapTransition())
        sm.add_widget(Activity(name='active'))
        sm.add_widget(Publicstatus(name='public_status'))
        sm.add_widget(Chats(name='chats'))
        sm.add_widget(Notifications(name='notifications'))
        sm.add_widget(Calls(name='call'))
        sm.add_widget(Myaccount())
        sm.add_widget(Mydocs())
        sm.add_widget(Mysecrets())
        return root
        Factory.register('videofiles', cls=videofiles)
        Factory.register('myprofile', cls=Myprofile)



#compling command  
if __name__ =='__main__':
    interactive = MasenoeasyApp()
    interactive.run()
