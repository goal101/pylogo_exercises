
import PyLogo.core.static_values as static
import PyLogo.core.utils as utils
from PyLogo.core.core_elements import World
from PyLogo.core.sim_engine import SimpleGUI

from itertools import cycle

from random import randint, random


class Starburst_World(World):
    """
    A starburst world of turtles.
    No special Patches or Turtles.
    """

    def setup(self, values):
        super().setup(values)

        nbr_turtles = int(values['nbr_turtles'])
        for i in range(nbr_turtles):
            # Adds itself to self.turtles and to its patch's list of Turtles.
            self.turtle_class()

        initial_velocities = cycle([utils.PixelVector2(-1, -1), utils.PixelVector2(-1, 1),
                                    utils.PixelVector2(0, 0),
                                    utils.PixelVector2(1, -1), utils.PixelVector2(1, 1)])
        for (turtle, vel) in zip(self.turtles, initial_velocities):
            turtle.velocity = vel


    def step(self, event, values):
        """
        Update the world by moving the turtles.
        """
        for turtle in self.turtles:
            turtle.move_by_velocity(values['Bounce?'])
            if static.TICKS > 200 and random() < 0.02:
                turtle.velocity = utils.PixelVector2(randint(-2, 2), randint(-2, 2))


def main():

    from PySimpleGUI import Checkbox, Slider, Text
    gui_elements = [Text('number of turtles'),
                    Slider(key='nbr_turtles', range=(1, 100), default_value=25,
                           orientation='horizontal', pad=((0, 50), (0, 20))),
                    Checkbox('Bounce?', key='Bounce?', default=True,
                             tooltip='Bounce back from the edges of the screen?')]

    simple_gui = SimpleGUI(gui_elements, caption='Starburst World')
    simple_gui.start(Starburst_World)


if __name__ == "__main__":
    main()