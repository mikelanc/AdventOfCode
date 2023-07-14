import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

class Day2AdventOfCode2022Test {

    private val testDay2 = Day2AdventOfCode2022()

    @Test
    fun singleScore_AV(){
        val expected = 8
        assertEquals(expected, testDay2.singleScore_2ndColIsPlay("A", "Y"))
    }

    @Test
    fun singleScore_BX(){
        val expected = 1
        assertEquals(expected, testDay2.singleScore_2ndColIsPlay("B", "X"))
    }

    @Test
    fun singleScore_CZ(){
        val expected = 6
        assertEquals(expected, testDay2.singleScore_2ndColIsPlay("C", "Z"))
    }

    @Test
    fun testFullScore() {
        val expected = 15
        assertEquals(expected, testDay2.fullScore_2ndColIsPlay(filename = "C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\test\\resources\\input_day2"))
    }

    @Test
    fun singleScore_2nd_AV(){
        val expected = 4
        assertEquals(expected, testDay2.singleScore_2ndColIsResult("A", "Y"))
    }

    @Test
    fun singleScore_2nd_BX(){
        val expected = 1
        assertEquals(expected, testDay2.singleScore_2ndColIsResult("B", "X"))
    }

    @Test
    fun singleScore_2nd_CZ(){
        val expected = 7
        assertEquals(expected, testDay2.singleScore_2ndColIsResult("C", "Z"))
    }

    @Test
    fun testFullScore_2nd() {
        val expected = 12
        assertEquals(expected, testDay2.fullScore_2ndColIsResult(filename = "C:\\Users\\mike\\IdeaProjects\\AdventOfCode\\src\\test\\resources\\input_day2"))
    }
}