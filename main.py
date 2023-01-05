from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
import datetime
import pygame

Window.size = (350, 600)


class Alarm(MDApp):
    def __init__(self):
        super().__init__()

    pygame.init()
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 0

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def get_time(self, instance, time):
        self.root.ids.alarm_time.text = str(time)

    def schedule(self, *args):
        Clock.schedule_once(self.alarm, 1)

    def alarm(self, *args):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if self.root.ids.alarm_time.text == str(current_time):
                self.start()
                break

    def set_volume(self, *args):
        self.volume += 0.05
        if self.volume < 1.0:
            Clock.schedule_interval(self.set_volume, 10)
            self.sound.set_volume(self.volume)
            print(self.volume)
        else:
            self.sound.set_volume(1)
            print("Reached max volume")

    def start(self, *args):
        self.sound.play(-1)
        self.set_volume()

    def stop(self):
        self.sound.stop()
        Clock.unschedule(self.set_volume)
        self.volume = 0

    def change_screen(self):
        self.root.current = "camera_screen"

    def build(self):
        return Builder.load_string('''
ScreenManager:
    id: screen_manager
    AlarmScreen:
        name: 'alarm_screen'
        id: alarm_screen
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            MDLabel:
                text: "ALARM CLOCK"
                font_size: "20sp"
                pos_hint: {"center_y": .935}
                halign: "center"
                bold: True
            MDIconButton:
                icon: "plus"
                pos_hint: {"center_x": .50, "center_y": .50}
                md_bg_color: 0, 0, 0, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                on_release: app.time_picker()
            MDLabel:
                id: alarm_time
                text: ""
                pos_hint: {"center_y": .7}
                halign: "center"
                font_size: "30sp"
                bold: True
            MDRaisedButton:
                text: "stop"
                pos_hint: {"center_x": .5, "center_y": .1}
                md_bg_color: 0, 0, 0, 1
                on_press: 
                    app.change_screen()
    CameraScreen:
        name: 'camera_screen'
        id: camera_screen
        MDFloatLayout:
        Camera:
            id: camera
            resolution: (640, 640)
            play: True
        MDIconButton:
            icon: "camera"
            pos_hint: {"center_x": .50, "center_y": .05}
            md_bg_color: 0, 0, 0, 1
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_press: camera.export_to_png('selfie.png')
'''

                                   )


class AlarmScreen(Screen):
    pass


class CameraScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(AlarmScreen(name='alarmscreen'))
sm.add_widget(CameraScreen(name='camerascreen'))

Alarm().run()
