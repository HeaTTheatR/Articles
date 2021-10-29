from kivymd.app import MDApp

from MeditationApp.Screens.RootScreen.root_screen import RootScreen


class MeditationAppLive(MDApp):
    def build(self):
        self.load_all_kv_files(self.directory)
        return RootScreen()


MeditationAppLive().run()
