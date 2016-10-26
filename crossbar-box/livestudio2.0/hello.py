from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks
from twisted.logger import Logger


class AppSession(ApplicationSession):

    log = Logger()

    slides = {
       'guid-1': ['eins', 'zwei', 'drei'],
       'guid-2': ['one', 'two', 'three'],
    }
    slide_ptr = {
        'guid-1': 0,
        'guid-2': 0
    }

    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def next_slide(guid):
            """
            increase slide pointer and publish new slide name
            :param guid: webcast id
            :type guid: str
            :return:
            """
            # can be replaced by REST API calls
            self.slide_ptr[guid] = min(self.slide_ptr[guid] + 1, len(self.slides[guid]) - 1)
            slide_pos = self.slide_ptr[guid]
            slide_set = self.slides[guid]
            slide_name = slide_set[slide_pos]

            self.publish('com.example.slide_updated.{0}'.format(guid), slide_name)

        def prev_slide(guid):
            """
            decrease slide pointer and publish new slide name
            :param guid: webcast id
            :type guid: str
            :return:
            """
            # can be replaced by REST API calls
            self.slide_ptr[guid] = max(0, self.slide_ptr[guid] - 1)
            slide_pos = self.slide_ptr[guid]
            slide_set = self.slides[guid]
            slide_name = slide_set[slide_pos]

            self.publish('com.example.slide_updated.{0}'.format(guid), slide_name)

        def current_slide(guid):
            """
            provide access to current active slide
            :param guid: webcast id
            :type guid: str
            :return: slide name of current active slide
            """
            # can be replaced by REST API calls
            slide_pos = self.slide_ptr[guid]
            slide_set = self.slides[guid]
            slide_name = slide_set[slide_pos]

            return slide_name

        yield self.register(next_slide, u'com.example.next_slide')
        yield self.register(prev_slide, u'com.example.prev_slide')
        yield self.register(current_slide, u'com.example.current_slide')
        print("procedures registered")

