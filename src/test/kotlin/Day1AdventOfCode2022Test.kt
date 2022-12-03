import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class Day1AdventOfCode2022Test {
    private val testDay1: Day1AdventOfCode2022 = Day1AdventOfCode2022()
    private val elvesCalories = testDay1.caloriesPerElfFromFile(filename="C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\test\\resources\\input_day1")

    @Test
    fun testHighest() {
        val expected = 24000
        assertEquals(expected, testDay1.findMostCaloriesElf(elvesCalories))
    }

    @Test
    fun testSumTop3() {
        val expected = 41000
        assertEquals(expected, testDay1.findSumOfCaloriesOfTopX(elvesCalories, 3))
    }
}