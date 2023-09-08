import java.util.Arrays;
// Basil Agboola
//Heuristic Attempt got way more moves sucessfully


class HeuristicKnight{

public static void main(String[] args){


    // Chess Board
int [][] Board = new int[][]     {{0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0}};

// Chess Board
// Heuristic Board
// I start from top left corner
int [][] HeuristicBoard = new int[][]     {{2,3,4,4,4,4,3,2},
                                           {3,4,6,6,6,6,4,3},
                                           {4,6,8,8,8,8,6,4},
                                           {4,6,8,8,8,8,6,4},
                                           {4,6,8,8,8,8,6,4},
                                           {4,6,8,8,8,8,6,4},
                                           {3,4,6,6,6,6,4,3},
                                           {2,3,4,4,4,4,3,2}};


                                  
// Heuristic Knight Object       
Heuristic thirdknight = new Heuristic();

//Using refrence variable to start tour

thirdknight.HeuristicTour();



}






}