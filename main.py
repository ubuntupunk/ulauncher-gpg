
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

class ulaunchergpg(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='ulaunchergpg',
                                         description='ulaunchergpg description',
                                         on_enter=HideWindowAction()))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='ulaunchergpg',
                                         description='ulaunchergpg description',
                                         on_enter=HideWindowAction()))

        return RenderResultListAction(items)


if __name__ == '__main__':
    ulaunchergpg().run()

