from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import webbrowser

class SujitMusicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Sujit Music Player", font_size='30sp'))
        self.search_input = TextInput(hint_text='Gana search karen...', multiline=False, font_size='25sp')
        layout.add_widget(self.search_input)
        play_btn = Button(text='Gana Bajao 🎶', background_color=(0, 1, 0, 1), font_size='25sp')
        play_btn.bind(on_press=self.play_music)
        layout.add_widget(play_btn)
        return layout

    def play_music(self, instance):
        song = self.search_input.text
        if song:
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

if __name__ == '__main__':
    SujitMusicApp().run()
    
