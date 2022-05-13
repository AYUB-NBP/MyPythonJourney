class rock(object):
    def __init__(self, color, roughness, size, state):
        self.color = color
        self.roughness = roughness
        self.size = size
        self.state = state

    def info(self):
        print(
            f"This rock is {self.color}, {self.roughness}, {self.size} and {self.state}")

    def split(self):
        self.state = 'Broken'


rock1 = rock('Blue', 'Soft', 'Small', 'Unified')
rock2 = rock('Grey', 'Rough', 'Big', 'Solid')
rock3 = rock('Green', 'Slippery', 'Medium', 'Crumbling')

rock.info(rock1)
rock.info(rock3)
print('-'*10)
print('Before:\n')
rock.info(rock2)
print("""
Splitting...
""")
rock.split(rock2)
print('After:\n')
rock.info(rock2)

