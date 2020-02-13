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

  def get_will_live_wrapper(self, item):
    x = item[0]
    y = item[1]
    return self.get_will_live(x,y)
  def get_will_live(self, x, y): 
    is_live = (x,y) in self.live_cords
    n_count = self.getNLive(self.getNine(x,y),x,y)
    return (is_live and n_count ==2) or n_count == 3

  def next(self):
    big_boy_set = set()
    for val in self.live_cords:
      x = val[0]
      y = val[0]
      big_boy_set.update(self.getNine(x,y))
    new_live= set(filter(self.get_will_live_wrapper, big_boy_set))
    print(new_live)
    return new_live
