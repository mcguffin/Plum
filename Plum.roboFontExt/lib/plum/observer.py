from mojo.events import addObserver, removeObserver

from plum import Plum


class PlumObserver(object):

    def __init__(self):
        addObserver(self, 'update', 'currentGlyphChanged')

    def update(self, info):
        Plum(info['glyph']).update()
