class SponsorHomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Welcome, Sponsor!'))
        update_button = Button(text='Update Profile', on_press=self.update_profile)
        layout.add_widget(update_button)
        self.add_widget(layout)
    
    def update_profile(self, instance):
        self.manager.current = 'sponsor_profile'