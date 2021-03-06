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
            size_hint : 1, 0.50
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
            text: "OPEN VIDEO UPLOADER"
            size_hint: 1, 0.10 
            background_color : 1, 0, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eleven'
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
            source : ""
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
            source : ""
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
    button_id : but
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : ""
            size_hint: 1, 0.70
        Button:
            id : but
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
                root.manager.current = 'screen_ten'
<ScreenTen>:
    image_id : img
    button_id : but
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : ""
            size_hint: 1, 0.70
        Button:
            text: "PROCESSING . . . ."
            id : but
            size_hint: 1, 0.10
            background_color : 0, 1, 1, 1
            text_color: 1,1,1,1
            on_press:
                root.play_video()
        Button: 
            text: "HOME"
            size_hint: 1, 0.10 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_home()
        Button: 
            text: "EXIT"
            size_hint: 1, 0.10 
            background_color : 1, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_exit()
<ScreenEleven>:
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
<ScreenTwelve>:
    image_id : img
    button_id : but
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : ""
            size_hint: 1, 0.70
        Button: 
            text: "PLAY"
            id : but
            size_hint: 1, 0.10 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.toggle_play()
        Button: 
            text: "CHOOSE A DIFFERENT VIDEO"
            size_hint: 1, 0.10 
            background_color : 0, 1, 1, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_eleven'
        Button: 
            text: "PERFORM YOLO"
            size_hint: 1, 0.10 
            background_color : 0, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_thirteen'
<ScreenThirteen>:
    image_id : img
    button_id : but
    BoxLayout:
        orientation: 'vertical'
        Image:
            id : img
            source : ""
            size_hint: 1, 0.70
        Button:
            text: "PROCESSING . . . ."
            id : but
            size_hint: 1, 0.10
            background_color : 0, 1, 1, 1
            text_color: 1,1,1,1
            on_press:
                root.play_video()
        Button: 
            text: "HOME"
            size_hint: 1, 0.10 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_home()
        Button: 
            text: "EXIT"
            size_hint: 1, 0.10 
            background_color : 1, 1, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.app_exit()
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
        self.button_id.text="START"
        self.start_flag=0
        self.stop_flag=0
        self.vid=cv2.VideoWriter("VIDEO1.avi",0,fourcc=cv2.VideoWriter_fourcc(*'MJPG'),fps=33,frameSize=(640,480))
    def update(self,dt):
        if self.cap.isOpened()==True:
            ret,frame=self.cap.read();
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
    def on_enter(self):
        self.video="VIDEO1.avi"
        self.capture=cv2.VideoCapture(self.video)
        self.start_flag=0
        self.stop_flag=0
        self.button_id.text="PLAY"
    def play_video(self):
        if(self.start_flag==0 and self.stop_flag==0):
            self.start_flag=1
            self.button_id.text="STOP"
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
        elif(self.start_flag==1 and self.stop_flag==0):
            self.stop_flag=1
            self.start_flag=0
            self.stop_video()
            self.button_id.text="PLAY"
        elif(self.start_flag==0 and self.stop_flag==1):
            self.start_flag=1
            self.stop_flag=0
            self.button_id.text="STOP"
            self.capture=cv2.VideoCapture(self.video)
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
    def update(self,dt):
        ret,frame=self.capture.read()
        #cv2.imshow("FRAME",frame)
        if(ret==False):
            self.stop_video()
            return
        cv2.imwrite("IMG3.png",frame)
        self.image_id.source="IMG3.png"
        self.image_id.reload()        
        pass
    def stop_video(self):
        Clock.unschedule(self.event)
        self.capture.release()
    def reset_video(self):
        #Clock.unschedule(self.event)
        os.remove(self.video)    
    pass
class ScreenTen(Screen):
    def on_enter(self):
            self.processed_flag=0
            self.start_flag=0
            self.stop_flag=0
            self.button_id.text="PROCESSING . . . ."
            self.video_orig="VIDEO1.avi"
            self.video_YOLO="VIDEO1_YOLO.avi"
            self.vid=cv2.VideoWriter(self.video_YOLO,0,fourcc=cv2.VideoWriter_fourcc(*'MJPG'),fps=33,frameSize=(640,480))
            self.capture1=cv2.VideoCapture(self.video_orig)
            self.capture2=cv2.VideoCapture(self.video_YOLO)
            self.per=Clock.schedule_interval(self.perform_YOLO,1.0/33.0)
    def perform_YOLO(self,dt):
            ret,frame=self.capture1.read()
            if(ret==False):
                self.processed_flag=1
                self.button_id.text="PLAY"
                Clock.unschedule(self.per)
                self.capture1.release()
                return
            cv2.imwrite("IMG3.png",frame)
            YOLO_object_detect("IMG3.png","IMG_YOLO3.png")
            frame2=cv2.imread("IMG_YOLO3.png")
            self.vid.write(frame2)
    def play_video(self):
        if(self.processed_flag==0):return

        if(self.start_flag==0 and self.stop_flag==0):
            self.start_flag=1
            self.button_id.text="STOP"
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
        elif(self.start_flag==1 and self.stop_flag==0):
            self.stop_flag=1
            self.start_flag=0
            self.stop_video()
            self.button_id.text="PLAY"
        elif(self.start_flag==0 and self.stop_flag==1):
            self.start_flag=1
            self.stop_flag=0
            self.button_id.text="STOP"
            self.capture2=cv2.VideoCapture(self.video_YOLO)
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
    def update(self,dt):
        ret,frame=self.capture2.read()
        #cv2.imshow("FRAME",frame)
        if(ret==False):
            self.stop_video()
            return
        cv2.imwrite("IMG3.png",frame)
        self.image_id.source="IMG3.png"
        self.image_id.reload()        
        pass
    def stop_video(self):
        Clock.unschedule(self.event)
        self.capture2.release()



    def app_home(self):
        os.remove("IMG3.png")
        os.remove("IMG_YOLO3.png")
        os.remove("VIDEO1.avi")
        os.remove("VIDEO1_YOLO.avi")
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1 
        self.manager.current = 'screen_one'
    def app_exit(self):
        os.remove("IMG3.png")
        os.remove("IMG_YOLO3.png")
        os.remove("VIDEO1.avi")
        os.remove("VIDEO1_YOLO.avi")
        exit(0)
    pass
class ScreenEleven(Screen):
    def save(self,path,text):
        print(text[-3:])
        os.system("cp "+str(text)+" VIDEO2.avi")
        time.sleep(1)
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1
        self.manager.current = 'screen_twelve'
    def cancel(self):
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1
        self.manager.current = 'screen_one'
    pass
class ScreenTwelve(Screen):
    def on_enter(self):
        self.video="VIDEO2.avi"
        self.capture=cv2.VideoCapture(self.video)
        self.start_flag=0
        self.stop_flag=0
        self.button_id.text="PLAY"
        self.image_id.source=""        
    def toggle_play(self):
        if(self.start_flag==0 and self.stop_flag==0):
            self.start_flag=1
            self.button_id.text="STOP"
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
        elif(self.start_flag==1 and self.stop_flag==0):
            self.stop_flag=1
            self.start_flag=0
            self.stop_video()
            self.button_id.text="PLAY"
        elif(self.start_flag==0 and self.stop_flag==1):
            self.start_flag=1
            self.stop_flag=0
            self.button_id.text="STOP"
            self.capture=cv2.VideoCapture(self.video)
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
    def update(self,dt):
        ret,frame=self.capture.read()
        #cv2.imshow("FRAME",frame)
        if(ret==False):
            self.stop_video()
            return
        cv2.imwrite("IMG3.png",frame)
        self.image_id.source="IMG3.png"
        self.image_id.reload()        
        pass
    def stop_video(self):
        Clock.unschedule(self.event)
        self.capture.release()
    def reset_video(self):
        #Clock.unschedule(self.event)
        os.remove(self.video)    
    pass
    pass
class ScreenThirteen(Screen):
    def on_enter(self):
            self.processed_flag=0
            self.start_flag=0
            self.stop_flag=0
            self.button_id.text="PROCESSING . . . ."
            self.video_orig="VIDEO2.avi"
            self.video_YOLO="VIDEO2_YOLO.avi"
            self.frame_h=0
            self.frame_w=0
            self.frames=[]
            
            self.capture1=cv2.VideoCapture(self.video_orig)
            self.capture2=cv2.VideoCapture(self.video_YOLO)
            self.per=Clock.schedule_interval(self.perform_YOLO,1.0/33.0)
    def perform_YOLO(self,dt):
            ret,frame=self.capture1.read()
            self.frame_h=frame.shape[0]
            self.frame_w=frame.shape[1]
            if(ret==False):
                self.processed_flag=1
                Clock.unschedule(self.per)
                self.capture1.release()
                return
            cv2.imwrite("IMG3.png",frame)
            YOLO_object_detect("IMG3.png","IMG_YOLO3.png")
            frame2=cv2.imread("IMG_YOLO3.png")
            self.frames.append(frame2)
            #self.vid.write(frame2)
    def play_video(self):
        if(self.processed_flag==0):return
        if(self.processed_flag==1):
        	self.vid=cv2.VideoWriter(self.video_YOLO,0,fourcc=cv2.VideoWriter_fourcc(*'MJPG'),fps=33,frameSize=(self.frame_h,self.frame_w))
        	for f in self.frames:
        		self.vid.write(f)
        	self.button_id.text="PLAY"
        	return

        if(self.start_flag==0 and self.stop_flag==0):
            self.start_flag=1
            self.button_id.text="STOP"
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
        elif(self.start_flag==1 and self.stop_flag==0):
            self.stop_flag=1
            self.start_flag=0
            self.stop_video()
            self.button_id.text="PLAY"
        elif(self.start_flag==0 and self.stop_flag==1):
            self.start_flag=1
            self.stop_flag=0
            self.button_id.text="STOP"
            self.capture2=cv2.VideoCapture(self.video_YOLO)
            self.event=Clock.schedule_interval(self.update, 1.0/33.0)
    def update(self,dt):
        ret,frame=self.capture2.read()
        #cv2.imshow("FRAME",frame)
        if(ret==False):
            self.stop_video()
            return
        cv2.imwrite("IMG3.png",frame)
        self.image_id.source="IMG3.png"
        self.image_id.reload()        
        pass
    def stop_video(self):
        Clock.unschedule(self.event)
        self.capture2.release()



    def app_home(self):
        os.remove("IMG3.png")
        os.remove("IMG_YOLO3.png")
        os.remove("VIDEO2.mp4")
        os.remove("VIDEO2_YOLO.mp4")
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 1 
        self.manager.current = 'screen_one'
    def app_exit(self):
        os.remove("IMG3.png")
        os.remove("IMG_YOLO3.png")
        os.remove("VIDEO2.mp4")
        os.remove("VIDEO2_YOLO.mp4")
        exit(0)
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
screen_manager.add_widget(ScreenTen(name ="screen_ten"))
screen_manager.add_widget(ScreenEleven(name ="screen_eleven"))    
screen_manager.add_widget(ScreenTwelve(name ="screen_twelve"))
screen_manager.add_widget(ScreenThirteen(name ="screen_thirteen"))   
# Create the App class 
class ScreenApp(App): 
    def build(self):
        return screen_manager 
  
# run the app  
sample_app = ScreenApp() 
sample_app.run()

