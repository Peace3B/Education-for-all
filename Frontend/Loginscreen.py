# Define Screens
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='Education for All - LOGIN'))
        self.username = TextInput(hint_text='Username')
        self.password = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        
        login_button = Button(text='Login', on_press=self.login)
        create_account_button = Button(text='Create Account', on_press=self.go_to_signup)
        
        layout.add_widget(login_button)
        layout.add_widget(create_account_button)
        self.add_widget(layout)
    

