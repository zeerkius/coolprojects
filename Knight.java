import java.util.Arrays;
public class Knight{
    int [] Row = {2,1,-1,-2,-2,-1,1,2};
    int [] Column = {-1,-2,-2,-1,1,2,2,1};
  

    int RowVar = 0;
    int ColumnVar = 0;
    int location = 1;
    boolean error = false;
    
    

     int [][] Board = new int[][] {{0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0}};
    
    


// Used this to see if it got the whole way ended up not working/
// To count to check if  It has been completley solved
public int countboard(int[][] chessboard){
    int count = 0;
    for (int i = 0; i < chessboard.length; i++){
        for (int j = 0; j < chessboard.length; j++){
            count += chessboard[i][j];
       }
    }
    return count;
    }




// Create Methods
// Brute Force Attempt Reaches 4 moves
public void startTour()
{
    
    //Does the tour
     // loops through and with every i it checkf if it is inside the board and can make the move 
    for (int i = 0; i < Board.length; i++ ){
        for (int j = 0; j < Board.length; j++){
        do{
            RowVar += Row[i];
            ColumnVar += Column[i];
            if((RowVar < 0 || RowVar > 7) || (ColumnVar < 0 || ColumnVar > 7)){
                RowVar = RowVar - Row[i];
                ColumnVar = ColumnVar - Column[i];
                error = true;
                continue;
                // It can make the move so it continues like that
            } 
            if (Board[RowVar][ColumnVar] == 0){
                Board[RowVar][ColumnVar] += location;
                location += 1;
                error = false;
            }

    
        }
        while(error == false);
    
    }

    }
    System.out.print(Arrays.deepToString(Board));

}



// Ended Up not using either of these methods
public int returnSpaceValue(int row, int column)
{
    int value = Board[row][column];
    return value;
}

public Boolean isKnightStuck(int row, int column)
{
    // Check all moves from here to see if knight is stuck.
    // If stuck, return true.
    Boolean isStuck = false;

    // If stuck, set true. 


    return isStuck;
}


}