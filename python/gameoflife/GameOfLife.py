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

  def get_will_live(self, x, y): 
    is_live = (x,y) in self.live_cords
    n_count = self.getNLive(self.getNine(x,y),x,y)
    return (is_live and n_count ==2) or n_count == 3


