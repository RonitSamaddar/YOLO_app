import os
import time
import cv2
import sys
# import kivy module     
import kivy   
       
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  

  
# Builder is used when .kv file is 
# to be used in .py file 
from kivy.lang import Builder 
  
# The screen manager is a widget 
# dedicated to managing multiple screens for your application. 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.clock import Clock

from converter import Converter
conv = Converter()

from YOLO_object_detection import YOLO_object_detect


   
# You can create your kv code in the Python file 
Builder.load_string(""" 
<ScreenOne>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "HELLO! WELCOME TO THE YOLO APP"
            size_hint : 1, 0.60
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1
        Button: 
            text: "CAPTURE IMAGE"
            size_hint: 1, 0.10
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_two'
        Button: 
            text: "CAPTURE VIDEO"
            size_hint: 1, 0.10
            background_color : 0, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eight'
        Button: 
            text: "OPEN IMAGE UPLOADER"
            size_hint: 1, 0.10 
            background_color : 0, 0, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five'
        Button: 
            text: "EXIT"
            size_hint: 1, 0.10 
            background_color : 1, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_exit()
<ScreenTwo>:
    img_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "Black.png"
            size_hint: 1, 0.80
        Button: 
            text: "CAPTURE"
            size_hint: 1, 0.20 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.capture()
<ScreenThree>:
    image_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "IMG1.png"
            size_hint: 1, 0.68
        Button: 
            text: "RETAKE PICTURE"
            size_hint: 1, 0.16 
            background_color : 0, 1, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_two'
        Button: 
            text: "PERFORM YOLO"
            size_hint: 1, 0.16 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four'
<ScreenFour>:
    image_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "IMG_YOLO1.png"
            size_hint: 1, 0.72
        Button: 
            text: "HOME"
            size_hint: 1, 0.14 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_home()
        Button: 
            text: "EXIT"
            size_hint: 1, 0.14 
            background_color : 1, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_exit()
<ScreenFive>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser
            on_selection: text_input.text = self.selection and self.selection[0] or ''

        TextInput:
            id: text_input
            size_hint_y: None
            height: 30
            multiline: False

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Save"
                on_release:
                    root.save(filechooser.path, text_input.text)
<ScreenSix>:
    image_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "IMG2.png"
            size_hint: 1, 0.68
        Button: 
            text: "CHOOSE A DIFFERENT PICTURE"
            size_hint: 1, 0.16 
            background_color : 0, 1, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five'
        Button: 
            text: "PERFORM YOLO"
            size_hint: 1, 0.16 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_seven'
<ScreenSeven>:
    image_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "IMG_YOLO2.png"
            size_hint: 1, 0.72
        Button: 
            text: "HOME"
            size_hint: 1, 0.14 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_home()
        Button: 
            text: "EXIT"
            size_hint: 1, 0.14 
            background_color : 1, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_exit()
<ScreenEight>:
    img_id : img
    button_id: but
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "Black.png"
            size_hint: 1, 0.80
        Button: 
            text: "START"
            id : but
            size_hint: 1, 0.20 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.toggle_capture()
<ScreenNine>:
    image_id : img
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : "Black.png"
            size_hint: 1, 0.70
        Button:
            text: "PLAY"
            size_hint: 1,0.10
            background_color: 1,0,1,1
            text_color: 1,1,1,1
            on_press:
                root.play_video()
        Button: 
            text: "RETAKE VIDEO"
            size_hint: 1, 0.16 
            background_color : 0, 1, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.reset_video()
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eight'
        Button: 
            text: "PERFORM YOLO"
            size_hint: 1, 0.16 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four'
""") 
   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen 
class ScreenOne(Screen):
    def app_exit(self):
        exit(0)
    pass

class ScreenTwo(Screen):

    #staticmethod

    def on_enter(self):
        self.cap=cv2.VideoCapture(0)
        self.event=Clock.schedule_interval(self.update, 1.0/33.0)
    def update(self,dt):
        if self.cap.isOpened()==True:
            ret,frame=self.cap.read();
            cv2.imwrite("IMG1.png",frame)
            self.img_id.source="IMG1.png"
            self.img_id.reload()
    def capture(self):
        Clock.unschedule(self.event)
        self.cap.release()        
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1
        self.manager.current = 'screen_three'
class ScreenThree(Screen):
    def on_enter(self):
            image=self.ids['img']
            image.reload()
    pass
class ScreenFour(Screen):
    def perform_YOLO(self):
            YOLO_object_detect("IMG1.png","IMG_YOLO1.png")
    def on_enter(self):
            self.perform_YOLO()
            image=self.ids['img']
            image.reload()
    def app_home(self):
        os.remove("IMG1.png")
        os.remove("IMG_YOLO1.png")
        os.system("rm -rf __pycache__")
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1 
        self.manager.current = 'screen_one'
    def app_exit(self):
        os.remove("IMG1.png")
        os.remove("IMG_YOLO1.png")
        os.system("rm -rf __pycache__")
        exit(0)
    pass
class ScreenFive(Screen):
    def save(self,path,text):
        os.system("cp "+str(text)+" IMG2.png")
        time.sleep(1)
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1
        self.manager.current = 'screen_six'
    def cancel(self):
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1
        self.manager.current = 'screen_one'
    pass
class ScreenSix(Screen):
    def on_enter(self):
            image=self.ids['img']
            image.reload()
    pass
class ScreenSeven(Screen):
    def perform_YOLO(self):
            YOLO_object_detect("IMG2.png","IMG_YOLO2.png")
    def on_enter(self):
            self.perform_YOLO()
            image=self.ids['img']
            image.reload()
    def app_home(self):
        os.remove("IMG2.png")
        os.remove("IMG_YOLO2.png")
        os.system("rm -rf __pycache__")
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1 
        self.manager.current = 'screen_one'
    def app_exit(self):
        os.remove("IMG2.png")
        os.remove("IMG_YOLO2.png")
        os.system("rm -rf __pycache__")
        exit(0)
    pass
class ScreenEight(Screen):
    def on_enter(self):
        self.cap=cv2.VideoCapture(0)
        self.event=Clock.schedule_interval(self.update, 1.0/33.0)
        self.start_flag=0
        self.stop_flag=0
        self.vid=cv2.VideoWriter("VIDEO1.mp4",0,fourcc=cv2.VideoWriter_fourcc(*'MP4V'),fps=33,frameSize=(480,640))
    def update(self,dt):
        if self.cap.isOpened()==True:
            ret,frame=self.cap.read();
            print(frame.shape)
            cv2.imwrite("IMG3.png",frame)
            self.img_id.source="IMG3.png"
            self.img_id.reload()
            if(self.start_flag==1):
                self.vid.write(frame)
    def toggle_capture(self):
        if(self.start_flag==0):
            #Video will start capturing
            self.start_flag=1
            self.button_id.text="STOP"
        elif(self.start_flag==1):
            #Video will stop capturing
            self.stop_flag=1 
            Clock.unschedule(self.event)
            self.cap.release()  
            self.vid.release()   
            self.manager.transition.direction = 'left' 
            self.manager.transition.duration = 1
            self.manager.current = 'screen_nine'
class ScreenNine(Screen):
    def play_video(self):
        pass
    def reset_video(self):
        os.remove("VIDEO1.mp4")
            
    pass


   
   
# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three")) 
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))
screen_manager.add_widget(ScreenSix(name ="screen_six"))
screen_manager.add_widget(ScreenSeven(name ="screen_seven"))
screen_manager.add_widget(ScreenEight(name ="screen_eight"))    
screen_manager.add_widget(ScreenNine(name ="screen_nine"))  
# Create the App class 
class ScreenApp(App): 
    def build(self):
        return screen_manager 
  
# run the app  
sample_app = ScreenApp() 
sample_app.run()

