import { expect } from 'chai';
import { isAlive } from './GameOfLife';

describe('GameOfLife', () => {
  it('should return true', () => {
    expect(isAlive()).to.be.true;
  });
});
