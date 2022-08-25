import java.util.*;
import java.lang.Math;
public class leetcode_1521 {
    public static void main(String[] args) {
        
    }

    public int closestToTarget(int[] arr, int target) {
        int len = arr.length;
        TreeSet<Integer> seen = new TreeSet<>();
        int ans = Integer.MAX_VALUE;
        for(int i=0; i<len; i++){
            seen.add(arr[i]);
            TreeSet<Integer> tmp = new TreeSet<>();
            Iterator<Integer> it = seen.iterator();
            while(it.hasNext()){
                int x = arr[i] & it.next();
                ans = Math.min(ans, Math.abs(x - target));
                tmp.add(x);
            }
            seen = tmp;
        }
        return ans;
    }
}
