from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks
from twisted.logger import Logger

class AppSession(ApplicationSession):

    log = Logger()


    slides = ['eins', 'zwei', 'drei']
    slide_ptr = 0

    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def next_slide():
            self.slide_ptr = min(self.slide_ptr + 1, len(self.slides) - 1)
            self.publish('com.example.slide_updated', self.slides[self.slide_ptr])

        def prev_slide():
            self.slide_ptr = max(0, self.slide_ptr - 1)
            self.publish('com.example.slide_updated', self.slides[self.slide_ptr])

        def get_slide():
            return self.slides[self.slide_ptr]

        yield self.register(next_slide, u'com.example.next_slide')
        yield self.register(prev_slide, u'com.example.prev_slide')
        yield self.register(get_slide, u'com.example.get_slide')
        print("procedures registered")
