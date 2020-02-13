from .context import gameoflife

def test_isAlive():
    game = gameoflife.GameOfLife(set([(1,1), (1,2)]))
    assert game.isAlive()

def test_isDead():
    game = gameoflife.GameOfLife(set())
    assert not game.isAlive()

def test_getNine():
    game = gameoflife.GameOfLife(set())
    neighbors = game.getNine(1,1)
    print(neighbors)
    assert neighbors == set([(0,0), (0,1) , (0,2), (1,0), (1,1) , (1,2), (2,0), (2,1) , (2,2)])