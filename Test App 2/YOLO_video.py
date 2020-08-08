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

from YOLO_object_detection import YOLO_object_detect

Builder.load_string(""" 
<ScreenOne>:
	img_id : img
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: "HELLO! WELCOME TO THE YOLO_VIDEO"
			size_hint : 1, 0.24
			text_color : 1, 1, 1, 1
		Image:
            id : img
            source : "Black.png"
            size_hint: 1, 0.75

""")

class ScreenOne(Screen):
	def on_enter(self):
		self.capture=cv2.VideoCapture(0)
		if self.capture.isOpened()==True:
			ret,frame=self.capture.read();
			cv2.imwrite("capture.png",frame)
			self.img_id.source="capture.png"
			self.img_id.reload()
	pass

# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 
screen_manager.add_widget(ScreenOne(name ="screen_one")) 

# Create the App class 
class ScreenApp(App): 
    def build(self):
        return screen_manager 
  
# run the app  
sample_app = ScreenApp() 
sample_app.run()