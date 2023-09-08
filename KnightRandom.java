import java.util.Arrays;
import java.util.Random;
public class KnightRandom{
    int [] Row = {2,1,-1,-2,-2,-1,1,2};
    int [] Column = {-1,-2,-2,-1,1,2,2,1};
  
    int RowVar = 0;
    int ColumnVar = 0;
    int location = 1;
    int temp = 0;
    int locater = 0;
    boolean error = false;
    
    

     int [][] Board = new int[][] {{0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0},
                                   {0,0,0,0,0,0,0,0}};
    
    
// Use this to find index of random value so I can get corresponding Column Value
public int FindIndex(int value){
    int [] RowH = {2,1,-1,-2,-2,-1,1,2};
    int index = 0;
    for (int i = 0; i < RowH.length; i++){
        if (RowH[i] == value ){
            index = i;
        }
    }
return index;
}
// This allows me to get a random number from the row array
public int getRandomArr(int[] arow){
    int num = 0;
    int randomnum = new Random().nextInt(arow.length);
    num = arow[randomnum];
    return num;


}



public void RandomTour(){
    // I looped 8^4 times to see how many moves i could squeeze out I only got 5
    // On some trials I got 6
    for (int i = 0; i < 4096; i++ ){
       for (int j = 0; j < 4096; j++){
        do{
            temp = getRandomArr(Row);
            RowVar += temp;
            locater = FindIndex(temp);
            ColumnVar += Column[locater];
            if(RowVar < 0 || RowVar > 7 || ColumnVar < 0 || ColumnVar > 7){
                RowVar = RowVar - Row[locater];
                ColumnVar = ColumnVar - Column[locater];
                error = true;
                temp = temp - temp;
                continue;

            } 
            if (Board[RowVar][ColumnVar] == 0){
               Board[RowVar][ColumnVar] += location;
                location += 1;
                error = false;
            }
             temp = temp - temp;
        }
        while(error == false);
    }
}

System.out.print(Arrays.deepToString(Board));
}

}
