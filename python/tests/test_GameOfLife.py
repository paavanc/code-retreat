from .context import gameoflife

def test_isAlive():
    gameOfLife = gameoflife.GameOfLife()
    assert gameOfLife.isAlive()
