import sbt.Keys._
import sbt._

object Settings {
  final val dependencies =
    libraryDependencies ++= Seq(
      "org.scalatest"     %% "scalatest"               % "3.0.4"  % Test,
      "org.scalamock"     %% "scalamock"               % "4.0.0"  % Test
    )
}
