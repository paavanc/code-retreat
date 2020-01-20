#' Game of life tick
#'
#' Generates the next generation of cells.
#'
#' @param cells Current generation of cells
#'
#' @return A list of cells representing the next generation
#' @examples
#'
#' tick(list()) # list()
#'
#' @export

tick <- function(cells) {
  cells[[1]] <- "wat"
  cells
}