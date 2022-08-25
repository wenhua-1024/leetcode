public class leetcode_1252 {
    public static void main(String[] args) {
        int m = 2;
        int n = 2;
        int[][] indices = {{0,0}, {1,1}};
        int res = oddCells(m, n, indices);
        System.out.println(res);
    }

    private static int oddCells(int m, int n, int[][] indices){
        int[] rows = new int[m];
        int[] cols = new int[n];
        for(int i=0; i<indices.length; i++){
            rows[indices[i][0]]++;
            cols[indices[i][1]]++;
        }
        int[] res = new int[4];
        for(int i=0; i<rows.length; i++){   
            if(rows[i]%2 == 1)
                res[0]++;
            else
                res[1]++;
        }

        for(int i=0; i<cols.length; i++){   
            if(cols[i]%2 == 1)
                res[2]++;
            else
                res[3]++;
        }
        int count = 0;
        count += res[0]*res[3] + res[2]*res[1];
        return count;
    }
}
