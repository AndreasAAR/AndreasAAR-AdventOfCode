import scala.io.Source
import scala.util.Using

object FileProcessor {
  def main(args: Array[String]): Unit = {
    val filePath = "./testdata.txt"

    Using(Source.fromFile(filePath)) { source =>
      val lines = source.getLines().toList

      // Perform operations on the lines
      val results = processLines(lines)

      // Print the results
      results.foreach(println)
    }.getOrElse {
      // Handle any exceptions, e.g., file not found
      println("An error occurred while processing the file.")
    }
  }

def processLines(lines: List[String]): List[Any] = {
    // Here, perform your specific operations on the lines
    // For example, you might want to parse, filter, map, etc.
    // Below is a simple example that just returns the lines as-is
    lines
  }
}