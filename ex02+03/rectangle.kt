package ex02

data class Point(
    val x: Int,
    val y: Int,
)

class Rectangle(p1: Point, p2: Point) {
    // Instead of defining a rectangule by two points located in oposite sides of rectangle's
    // diagonal, we define this rectangles by two vertical lines and two horizontal lines in
    // the cartesian plane and with the four lines together, they can define the rectangles
    // limits
    var horizontalIni: Int = 0
    var horizontalEnd: Int = 0
    var verticalIni: Int = 0
    var verticalEnd: Int = 0

    // Converting the way of representing the rectangle to the way of using four lines - half of them
    // are in vertical direction and the other half are in horizontal direction:
    // .x1........x2.
    // .|..........|.
    // _|__________|_y2           y1 = verticalEnd
    // .|..........|.             y2 = verticalIni
    // .|..........|.             x1 = horizontalIni
    // .|..........|.             x2 = horizontalEnd
    // .|..........|.
    // _|__________|_y1
    // .|..........|.
    // .|..........|.

    init {
        if (p1.x > p2.x) {
            horizontalIni = p2.x
            horizontalEnd = p1.x
        } else {
            horizontalIni = p1.x
            horizontalEnd = p2.x
        }
        if (p1.y > p2.y) {
            verticalIni = p2.y
            verticalEnd = p1.y
        } else {
            verticalIni = p1.y
            verticalEnd = p2.y
        }
    }

    // There are four possibilities that results in no intersection between two rectangles
    // if you think in intersection between the horizontal and vertical limits of the
    // rectangles
    fun intersected(b: Rectangle): Boolean {
        return ! (
            this.horizontalIni > b.horizontalEnd ||
                this.horizontalEnd < b.horizontalIni ||
                this.verticalIni > b.verticalEnd ||
                this.verticalEnd < b.verticalIni
            )
    }

    // First we check if the rectangles intersects with each other:
    // - Yes, they do. Then the area will be the multiplication of the lengths in horizontal and in
    //   vertical intersections
    // - No, they don't. Then the area is simply 0
    fun intersectedArea(b: Rectangle): Int {
        if (this.intersected(b)) {
            val vIni = maxOf(this.verticalIni, b.verticalIni)
            val vEnd = minOf(this.verticalEnd, b.verticalEnd)
            val hIni = maxOf(this.horizontalIni, b.horizontalIni)
            val hEnd = minOf(this.horizontalEnd, b.horizontalEnd)
            return (vEnd - vIni + 1) * (hEnd - hIni + 1)
        } else {
            return 0
        }
    }
}

fun main(args: Array<String>) {
    if (args.size != 9) {
        println("Error, we need 9 arguments but ${args.size} were given.")
    } else {
        val A = Rectangle(
            Point(args[1].toInt(), args[2].toInt()),
            Point(args[3].toInt(), args[4].toInt())
        )

        val B = Rectangle(
            Point(args[5].toInt(), args[6].toInt()),
            Point(args[7].toInt(), args[8].toInt())
        )

        if (args[0] == "boolean") {
            println(A.intersected(B))
        } else if (args[0] == "area") {
            println(A.intersectedArea(B))
        } else {
            println("Error: option ${args[0]} is not valid")
            println("Possible values are 'boolean' and 'area'")
        }
    }
}
