import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada Or Potato!"
GAME_SPEED = 1/60
ADA_IMAGE = arcade.load_texture("images/ada.png")
POTATO_IMAGE = arcade.load_texture("images/potato.png")


class AdaPotato(arcade.Sprite):
    timer: int
    score: int

    def __init__(self):
        super().__init__()
        self.texture = ADA_IMAGE
        self.score = 0
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2

    def mousepress(self):
        if self.texture == ADA_IMAGE:
            self.score += 1
        if self.texture == POTATO_IMAGE:
            self.score -= 1

    def draw(self):
        pass

    def update(self):
        self.timer += 1
        print(self.score)
        if self.timer > 60:
            if self.texture == ADA_IMAGE:
                self.texture = POTATO_IMAGE
                self.timer = 0
            elif self.texture == POTATO_IMAGE:
                self.texture = ADA_IMAGE
                self.timer = 0


class Window(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.ada_potato = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.ada_potato = arcade.SpriteList()
        self.ada_potato.append(AdaPotato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.ada_potato.draw()

    def on_update(self, delta_time):
        self.ada_potato.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.ada_potato.mousepress()


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
