package com.gameoflife

import org.scalatest.{FreeSpecLike, Matchers}

class GameoflifeServiceSpec extends FreeSpecLike with Matchers {
  "GameoOfLife" - {
    "Should return true" in {
      GameOfLife.alive shouldBe true
    }
  }
}
