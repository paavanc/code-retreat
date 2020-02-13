class GameOfLife:

  def __init__(self, live_cords = set()):
    self.live_cords = live_cords

  def isAlive(self):
    if self.live_cords:
      return True
    return False

  def getNine(self, x, y):
    result = set()
    for i in range(x-1, x+2):
      for j in range(y-1, y+2):
        result.add((i,j))
    return result

  def getNLive(self, neighbors, x, y):
    neighbors.remove((x,y))
    return len(neighbors.intersection(self.live_cords))



