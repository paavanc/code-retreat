context("gameoflife::tick")

testthat::test_that("returns no cells when the world is empty", {
  testthat::expect_equal(
    tick(list()),
    list()
  )
})
