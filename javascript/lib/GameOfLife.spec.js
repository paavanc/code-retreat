const GameOfLife = require('./GameOfLife')
const expect = require('chai').expect

describe('GameOfLife', () => {
  it('should return true', () => {
    expect(GameOfLife.isAlive()).to.be.true;
  })
})
