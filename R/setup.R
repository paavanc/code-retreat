working_directory <- getwd()
package <- "gameoflife"
me <- "Alex Codreanu"
package_dir <- paste0(working_directory, "/", package)

print(package_dir)

usethis::create_package(package_dir)
usethis::use_mit_license(name = me)
usethis::use_readme_rmd()
usethis::use_testthat()
usethis::use_pipe()
