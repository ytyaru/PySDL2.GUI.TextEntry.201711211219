import sys
import sdl2
import sdl2.ext

#http://pysdl2.readthedocs.io/en/rel_0_9_4/modules/sdl2ext_gui.html
#https://translate.google.com/translate?sl=en&tl=ja&js=y&prev=_t&hl=ja&ie=UTF-8&u=http%3A%2F%2Fpysdl2.readthedocs.io%2Fen%2Frel_0_9_4%2Fmodules%2Fsdl2ext_gui.html&edit-text=&act=url

GREY = sdl2.ext.Color(200, 200, 200)
RED = sdl2.ext.Color(255, 0, 0)
GREEN = sdl2.ext.Color(0, 255, 0)

def onInput(ui, event):
    print("Input: ", ui, event)
def onEditing(ui, event):
    print("Editing: ", ui, event)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("PySDL2でTextEntryを作る", size=(800, 600))
    window.show()
    
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    uifactory = sdl2.ext.UIFactory(factory)
    entry = uifactory.from_color(sdl2.ext.TEXTENTRY, color=GREY, size=(300,50))
    entry.position = 50, 50
    entry.input += onInput
    entry.editing += onEditing

    spriterenderer = factory.create_sprite_render_system(window)
    uiprocessor = sdl2.ext.UIProcessor()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            uiprocessor.dispatch([entry], event)
        spriterenderer.render((entry, ))

if __name__ == "__main__":
    sys.exit(run())
