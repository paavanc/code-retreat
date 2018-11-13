package com.gameoflife;

import org.junit.Test;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class GameOfLifeTest {

    @Test
    public void alive() {
        assertThat(GameOfLife.isAlive(), is(true));
    }
}