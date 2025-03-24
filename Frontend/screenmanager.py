# Screen Manager
class SponsorshipApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(SponsorHomeScreen(name='sponsor_home'))
        sm.add_widget(SponsorProfileScreen(name='sponsor_profile'))
        return sm

if __name__ == '__main__':
    SponsorshipApp().run()