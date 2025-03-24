# Signup Screen
class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='Education for All - CREATE ACCOUNT'))
        self.username = TextInput(hint_text='Username')
        self.email = TextInput(hint_text='Email')
        self.password = TextInput(hint_text='Password', password=True)
        
        layout.add_widget(self.username)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        
        signup_button = Button(text='Create Account', on_press=self.create_account)
        layout.add_widget(signup_button)
        self.add_widget(layout)
    
    def create_account(self, instance):
        print(f'Creating account for {self.username.text}')
        self.manager.current = 'login'