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

def test_get_live_count():
    game = gameoflife.GameOfLife(set([(0,0) , (0,2) , (1,1)]))
    neighbors = game.getNine(1,1)
    assert 2 == game.getNLive(neighbors, 1, 1)

def test_will_live():
    game = gameoflife.GameOfLife(set([(0,0) , (0,2) , (0,1)]))
    
    assert game.get_will_live(0,1)

def test_will_live():
    game = gameoflife.GameOfLife(set([(0,0) , (0,2) , (0,1)]))
    
    assert not game.get_will_live(4,4)

def test_mutate():
    game = gameoflife.GameOfLife(set([(0,0) , (0,1) , (0,2)]))

    next = game.next()
    assert len(next) == 3


