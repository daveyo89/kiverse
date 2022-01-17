import kivy
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest

kivy.require('2.0.0')


class KivyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main.kv')

    def build(self):
        self.screen.ids.text_field.bind(
            on_text_validate=self.make_request,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True

    def make_request(self, *args):
        slug = self.screen.ids.text_field.text

        UrlRequest(
            url='dummyurl',
            on_error=None,
            on_failure=self.on_request_failure,
            on_progress=None,
            on_redirect=None,
            on_success=self.on_request_success,
            timeout=3,
        )

    def on_request_success(self, request, result):
        self.root.ids['scroll_text'].text = result.get('content', '')

    def on_request_failure(self, request, result):
        self.root.ids['scroll_text'].text = "Request Failed."


KivyApp().run()
