class RandomTour{


//Basil Agboola
//2aBrute-Force Knight Tour application, 15pts
// Starts at Top Corner and marks it with zero 
// Makes 5 moves after

// Chess Board
int [][] Board = new int[][]     {{0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0},
                                  {0,0,0,0,0,0,0,0}};



public static void main(String[] args){

KnightRandom secondKnight = new KnightRandom();

secondKnight.RandomTour();
}
}