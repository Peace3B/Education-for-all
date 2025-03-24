# Sponsor Profile Screen
class SponsorProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Update Your Profile'))
        
        self.name = TextInput(hint_text='Name')
        self.gender = TextInput(hint_text='Gender')
        self.preferences = TextInput(hint_text='Preferences for age/location')
        
        layout.add_widget(self.name)
        layout.add_widget(self.gender)
        layout.add_widget(self.preferences)
        
        save_button = Button(text='Save', on_press=self.save_profile)
        layout.add_widget(save_button)
        self.add_widget(layout)
    
    def save_profile(self, instance):
        print(f'Profile saved: {self.name.text}, {self.gender.text}, {self.preferences.text}')
        self.manager.current = 'sponsor_home'
