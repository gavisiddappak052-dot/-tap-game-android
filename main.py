
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TapGame(App):
    def build(self):
        self.score = 0
        self.time_left = 30

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        self.label = Label(
            text="Score: 0",
            font_size=30
        )

        self.timer = Label(
            text="Time: 30",
            font_size=25
        )

        self.tap_button = Button(
            text="TAP ME!",
            font_size=30
        )
        self.tap_button.bind(on_press=self.tap)

        restart_button = Button(
            text="RESTART",
            font_size=22
        )
        restart_button.bind(on_press=self.restart)

        layout.add_widget(self.label)
        layout.add_widget(self.timer)
        layout.add_widget(self.tap_button)
        layout.add_widget(restart_button)

        self.clock_event = None
        self.start_timer()

        return layout

    def tap(self, instance):
        if self.time_left > 0:
            self.score += 1
            self.label.text = f"Score: {self.score}"

    def start_timer(self):
        self.clock_event = Clock.schedule_interval(
            self.countdown, 1
        )

    def countdown(self, dt):
        self.time_left -= 1
        self.timer.text = f"Time: {self.time_left}"

        if self.time_left <= 0:
            self.timer.text = "Time Up!"
            self.tap_button.disabled = True
            return False

    def restart(self, instance):
        if self.clock_event:
            self.clock_event.cancel()

        self.score = 0
        self.time_left = 30
        self.label.text = "Score: 0"
        self.timer.text = "Time: 30"
        self.tap_button.disabled = False
        self.start_timer()


TapGame().run()
()