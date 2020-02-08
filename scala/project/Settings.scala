import sbt.Keys._
import sbt._

object Settings {
  final val dependencies =
    libraryDependencies ++= Seq(
      "org.specs2" %% "specs2-core" % "4.8.3" % Test,
      "org.specs2" %% "specs2-mock" % "4.8.3" % Test
  )
}
