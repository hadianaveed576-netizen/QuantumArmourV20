from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.15, 1)

class QuantumApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text='QUANTUM ARMOUR V20\nULTIMATE PROTECTION', font_size='22sp', bold=True, color=(0,1,0.8,1), size_hint_y=0.3)
        
        status = Label(text='Status: ARMOUR ACTIVE\nThreats Blocked: 0\nSystem: Secure', font_size='18sp', color=(1,1,1,1))
        
        btn = Button(text='ACTIVATE QUANTUM SHIELD', font_size='20sp', background_color=(0,0.8,0.6,1), size_hint_y=0.25)
        btn.bind(on_press=lambda x: setattr(status, 'text', 'Status: SHIELD MAX POWER!\nThreats Blocked: 999+\nSystem: INVINCIBLE V20'))
        
        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(btn)
        return layout

QuantumApp().run()
