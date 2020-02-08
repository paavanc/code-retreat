package com.gameoflife

import org.specs2.matcher.Matchers
import org.specs2.mock.Mockito
import org.specs2.mutable.Specification


class GameOfLifeSpec extends Specification with Matchers with Mockito {
  "GameOfLife" >> {
    "Should return true" >> {
      GameOfLife.alive shouldEqual true
    }
  }
}
