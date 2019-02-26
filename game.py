from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.audio import SoundLoader

import os

from algorithm import *
from config import FIELD_WIDTH, FIELD_HEIGHT
from main import Game, Wall, Food, SnakeHead, SnakeTail

PATH_TO_PICTURES = "img"
BACKGROUND_IMAGE = "_G9aI67R2tQ.jpg"
BELKI = "belki.png"


Config.set('graphics','resizable','0')
Config.set('graphics','width','1200')
Config.set('graphics','height','600')

BUTTON_COLOR = [.97,.69,.59,1]


class MainApp(App):
    def build(self):
        sound = SoundLoader.load('muzlome_Metallica_-_Sad_But_True_47954412.mp3')
        sound.play()

        self.create_start_screen()
        self.create_game_screen()

        self.main_layout = FloatLayout()
        self.main_layout.add_widget(self.start_screen)
        return self.main_layout

    def create_start_screen(self):
        self.start_screen = FloatLayout(
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        background_image = Image(
            source=BACKGROUND_IMAGE,
            size_hint=[1, 1],
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=False
        )
        background_belki = Image(
            source=BELKI,
            size_hint=[1, 1],
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=False
        )

        buttons = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint=(0.3, 0.4),
            pos_hint={'center_x': 0.7, 'center_y': 0.4}
        )

        start_game_button = Button(
            text='Start game',
            on_press=self.reset_game_mode,
            background_normal='',
            background_color=BUTTON_COLOR,
            color=[0, 0, 0, 1]
        )

        settings_button = Button(
            text='Settings',
            #on_press=None,
            background_normal='',
            background_color=BUTTON_COLOR,
            color=[0, 0, 0, 1]
        )

        buttons.add_widget(start_game_button)
        buttons.add_widget(settings_button)

        self.start_screen.add_widget(background_image)
        self.start_screen.add_widget(buttons)

    def create_game_screen(self):
        self.board = BoardWidget(FIELD_WIDTH, FIELD_HEIGHT)

        exit_button = Button(
            text='Quit', on_press=self.leave,
            size_hint=[0.25, 0.1], pos_hint={'center_x': 1.30, 'center_y': 0.66},
            background_color=BUTTON_COLOR, background_normal=''
        )
        restart_button = Button(
            text='Restart', on_press=self.reset_game_mode,
            size_hint=[0.25, 0.1], pos_hint={'center_x': 1.30, 'center_y': 0.90},
            background_color=BUTTON_COLOR, background_normal=''
        )
        back_to_menu_button = Button(
            text='Main menu', #on_press=self.back_to_main_menu,
            size_hint=[0.25, 0.1], pos_hint={'center_x': 1.30, 'center_y': 0.78},
            background_color=BUTTON_COLOR, background_normal=''
        )

        make_move_button = Button(
            text='Make move', on_press=self.make_move,
            size_hint=[0.25, 0.1], pos_hint={'center_x': 1.30, 'center_y': 0.4},
            background_color=BUTTON_COLOR, background_normal=''
        )

        self.game_screen = FloatLayout(
            size_hint=[0.5, 1],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.game_screen.add_widget(self.board)
        self.game_screen.add_widget(exit_button)
        self.game_screen.add_widget(restart_button)
        self.game_screen.add_widget(back_to_menu_button)
        self.game_screen.add_widget(make_move_button)

    def reset_game_mode(self, _):
        self.game = Game()
        self.game.create_snake(alg=RandomAlgorithm(), pos=[2, 8])

        self.main_layout.remove_widget(self.main_layout.children[0])
        self.main_layout.add_widget(self.game_screen)

    def make_move(self, _): # FIXME not class method
        if self.game.is_game_over() == False:
            self.game.move()
        self.board.refresh(self.game.board)

    def set_start_mode(self, _):
        pass

    def leave(self, button):
        exit()


class BoardWidget(GridLayout):
    def __init__(self, width, height):
        # create a grid with nothings width x height.
        # store cell elements in self.image_board for convenience.
        super().__init__(
            pos_hint={'center_x':0.4,'center_y':0.5},
            size_hint=(FIELD_WIDTH/FIELD_HEIGHT, 1),
            cols=FIELD_WIDTH,
            rows=FIELD_HEIGHT
        )
        self.image_board = []
        for _ in range(FIELD_HEIGHT):
            image_line = []
            for _ in range(FIELD_WIDTH):
                current = Image(
                    source='', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                self.add_widget(current)
                image_line.append(current)
            self.image_board.append(image_line)

    def refresh(self, game_board):
        type_to_picture = { # FIXME: consider snake directions
            type(None): 'nothing.png',
            SnakeHead: 'head_right.png',
            SnakeTail: 'hor.png',
            Wall: 'tree.png',
            Food: 'food.png'
        }

        # assert not shit
        assert(len(self.image_board) == game_board.width)
        assert(len(self.image_board[0]) == game_board.length)

        field = game_board.field()
        # reset image sources for all cell widgets
        for i in range(game_board.width):
            for j in range(game_board.length):
                self.image_board[i][j].source = os.path.join(
                    PATH_TO_PICTURES,
                    type_to_picture[type(field[i][j])]
                )


if __name__ == '__main__':
    MainApp().run()
