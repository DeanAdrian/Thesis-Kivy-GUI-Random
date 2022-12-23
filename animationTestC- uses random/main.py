from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random


class SafeklistaApp(MDApp):

    def animate_the_widget(self, *args):
        widget = self.root.ids.left_animation
        anim = Animation(animated_color=(1, 0, 0, 0.8), blink_size=400, d=0.3) + Animation(animated_color=(1, 0, 0, 0),
                                                                                           blink_size=900, d=0.5)
        anim.bind(on_complete=self.reset)
        anim.start(widget)

    def animate_the_widget2(self, *args):
        widget = self.root.ids.back_animation
        anim = Animation(animated_color=(1, 0, 0, 0.8), blink_size=400, d=0.3) + Animation(animated_color=(1, 0, 0, 0),
                                                                                           blink_size=900, d=0.5)
        anim.bind(on_complete=self.reset)
        anim.start(widget)

    def animate_the_widget3(self, *args):
        widget = self.root.ids.right_animation
        anim = Animation(animated_color=(1, 0, 0, 0.8), blink_size=400, d=0.3) + Animation(animated_color=(1, 0, 0, 0),
                                                                                           blink_size=900, d=0.5)
        anim.bind(on_complete=self.reset)
        anim.start(widget)

    def leftalertSound(*args):
        sound = SoundLoader.load('mixkit-elevator-tone-2863(left_channel).wav')
        sound.play()

    def rightalertSound(*args):
        sound = SoundLoader.load('mixkit-elevator-tone-2863(right_channel).wav')
        sound.play()

    def backalertSound(*args):
        sound = SoundLoader.load('mixkit-elevator-tone-2863(back_channel).wav')
        sound.play()

    def reset(self, *args):
        widget = args[1]
        widget.animated_color = (1, 1, 1, 1)
        widget.blink_size = 0

    def generate_random_number(self, *args):
        # Generate a random number from 1 to 10
        random_number = random.randint(1, 4)

        if random_number == 2:
            Clock.schedule_once(self.animate_the_widget)
            # Clock.schedule_once(self.leftalertSound)
            print("left")
        elif random_number == 3:
            Clock.schedule_once(self.animate_the_widget2)
            # Clock.schedule_once(self.backalertSound)

            print("back")
        elif random_number == 4:
            Clock.schedule_once(self.animate_the_widget3)
            # Clock.schedule_once(self.rightalertSound)
            print("right")
        else:
            print(random_number)

    def build(self):
        # Clock.schedule_interval(self.animate_the_widget, 2)
        Clock.schedule_interval(self.generate_random_number, 0.5)
        return Builder.load_file('myapp.kv')


if __name__ == "__main__":
    SafeklistaApp().run()
