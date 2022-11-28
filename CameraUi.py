from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class camera_app(App):
    def make(self):
        self.obj_camera = Camera()
        self.obj_camera.resolution = (810, 810)
        obj_button = Button(text="Click!")
        obj_button.size_hint = (.6, .3)
        obj_button.pos_hint = {'x': .35, 'y': .35}
        obj_button.bind(on_press=self.selfie())
        obj_layout = BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
        return obj_layout

    def selfie(self, *args):
        print("Selfie has been taken")
        self.obj_camera.export_to_png('./demoselfie.png')


if __name__ == '__main__':
    camera_app().run()
