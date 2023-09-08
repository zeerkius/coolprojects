import java.util.Arrays;

class KnightsTour
{

//Basil Agboola
//BruteForce/ Basic Application 1b Attempt 25pts
// Starts at Top Corner and marks it with zero 
//Then makes 4 moves after


public static void main(String[] args)
{
// Chess Board
int [][] Board = new int[][]     {{0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0}};

// Where I will start the night ( Top left corner of the board)
// Declaring Knight Object
Knight firstKnight = new Knight();

// Using refrence Variable to Start the tour
firstKnight.startTour();







}
}