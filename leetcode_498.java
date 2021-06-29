public class leetcode_498 {
    public static void main(String[] args) {
        int[][] mat = {{1,2,3},{4,5,6},{7,8,9}};
        int[] res = findDiagonalOrder(mat);
        for(int i=0; i<res.length; i++)
            System.out.println(res[i]);
    }
    public static int[] findDiagonalOrder(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;
        int[] res = new int[col*row];
        int s=0;
        int i=0;
        int flag = 0;
        while(flag<(row+col-1)){
            if(flag%2 == 0){
                i=0;
                while(i<=flag & i<col){
                    if(flag-i<row & i<col)
                        res[s++] = mat[flag-i][i];
                    i++;
                }
                    
            }
            else{
                i=flag;
                while(i>=0){
                    if(flag-i<row & i<col)
                        res[s++] = mat[flag-i][i];
                    i--;
                }    
            }
            flag++;
        }
        return res;
    }
}
