resolvers in ThisBuild ++= Seq(
  Resolver.jcenterRepo
)

scalaVersion := "2.12.9"

lazy val root =
  (project in file("."))
   .settings(Settings.dependencies)


