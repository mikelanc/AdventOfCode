import java.io.File

fun main(args: Array<String>) {
    when (args[0]) {
        "1" -> {
            Day1AdventOfCode2022()
        }
        "2" -> {
            Day2AdventOfCode2022()
        }
        "3" -> {
        }
        "0" -> {
            Day1AdventOfCode2022()
            Day2AdventOfCode2022()
        }
    }
}

class Day1AdventOfCode2022 {
    init {
        val elvesCalories =
            this.caloriesPerElfFromFile(filename = "C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\main\\resources\\input_day1")
        println(this.findMostCaloriesElf(elvesCalories))
        println(this.findSumOfCaloriesOfTopX(elvesCalories, 3))
    }
    fun caloriesPerElfFromFile(filename:String): MutableList<Int> {
        var elvesCalories = mutableListOf<Int>()
        var calorieCount = 0

        File(filename).forEachLine {
            if (it == "") {
                elvesCalories += calorieCount
                calorieCount = 0
            } else {
                calorieCount += it.toInt()
            }
        }
        elvesCalories = elvesCalories.sorted().reversed().toMutableList()
        return elvesCalories
    }

    fun findMostCaloriesElf(elvesCalories: MutableList<Int>): Int {
        return elvesCalories.first()
    }

    fun findSumOfCaloriesOfTopX(elvesCalories: MutableList<Int>, topX: Int): Int {
        //val sortedList = elvesCalories.sorted().reversed()
        /*println(elvesCalories)
        var sum = 0
        for (i in 0..(topX -1))
            sum += elvesCalories[i]
        //return sum*/
        return elvesCalories.take(3).sum()
    }
}

class Day2AdventOfCode2022 {
    init {
        println(this.fullScore_2ndColIsPlay(filename="C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\main\\resources\\input_day2"))
        println(this.fullScore_2ndColIsResult(filename="C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\main\\resources\\input_day2"))
    }
    fun singleScore_2ndColIsPlay(opponentPlay: String, myPlay: String): Int {
        var myScore = 0
        var scoresForPlay = mapOf(
            "X" to 1,
            "Y" to 2,
            "Z" to 3
        )
        val scoresForResult = mapOf(
            "AX" to 3,
            "AY" to 6,
            "AZ" to 0,
            "BX" to 0,
            "BY" to 3,
            "BZ" to 6,
            "CX" to 6,
            "CY" to 0,
            "CZ" to 3,
        )
        myScore += scoresForPlay[myPlay] ?: 0
        myScore += scoresForResult[opponentPlay + myPlay] ?: 0
        return myScore
    }

    fun singleScore_2ndColIsResult(opponentPlay: String, myPlay: String): Int {
        var myScore = 0

        val scoresForResult = mapOf(
            "AX" to 3,
            "AY" to 4,
            "AZ" to 8,
            "BX" to 1,
            "BY" to 5,
            "BZ" to 9,
            "CX" to 2,
            "CY" to 6,
            "CZ" to 7
        )
        myScore += scoresForResult[opponentPlay + myPlay] ?: 0
        return myScore
    }


    fun fullScore_2ndColIsPlay(filename: String): Int{
        var myScore = 0

        File(filename).forEachLine {
            myScore += singleScore_2ndColIsPlay(it[0].toString(), it[2].toString())
        }
        return myScore
    }

    fun fullScore_2ndColIsResult(filename: String): Int{
        var myScore = 0

        File(filename).forEachLine {
            myScore += singleScore_2ndColIsResult(it[0].toString(), it[2].toString())
        }
        return myScore
    }

}