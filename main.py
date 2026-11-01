from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.15, 1)

class QuantumApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text='QUANTUM ARMOUR V20', font_size='24sp', bold=True)
        
        self.status = Label(text='Status: ARMOUR INACTIVE', font_size='18sp')
        
        btn = Button(text='ACTIVATE QUANTUM SHIELD', size_hint=(1, 0.3), background_color=(0, 0.8, 0.9, 1))
        btn.bind(on_press=self.activate)

        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        return layout
    
    def activate(self, instance):
        self.status.text = 'Status: ARMOUR ACTIVE - SHIELD ON!'

QuantumApp().run()
