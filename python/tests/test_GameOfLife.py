from .context import gameoflife

def test_isAlive():
    game = gameoflife.GameOfLife(set([(1,1), (1,2)]))
    assert game.isAlive()

def test_isDead():
    game = gameoflife.GameOfLife(set())
    assert not game.isAlive()
