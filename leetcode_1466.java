import java.util.HashSet;

public class leetcode_1466 {
    public int minReorder(int n, int[][] connections){
        int count = 0;
        HashSet<Integer> set = new HashSet<>();
        set.add(0);
        while(set.size()<n){
            for(int i=0; i<connections.length; i++){
                if(set.contains(connections[i][1])){
                    set.add(connections[i][0]);
                }
                else if(set.contains(connections[i][0])){
                    set.add(connections[i][1]);
                    count++;
                }
            }
        }
        return count;
    }
}
