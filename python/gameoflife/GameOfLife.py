class GameOfLife:

  def __init__(self, live_cords = set()):
    self.live_cords = live_cords

  def isAlive(self):
    if self.live_cords:
      return True
    return False
