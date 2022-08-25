import java.util.*;
public class leetcode_3 {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        Queue<Character> set = new LinkedList<>();
        for(int i=0; i<s.length(); i++){
            if(set.contains(s.charAt(i))){
                while(set.contains(s.charAt(i))){
                    set.poll();
                }
                set.add(s.charAt(i));
                continue;
            }
            set.add(s.charAt(i));
            res = Math.max(res, set.size());
        }
        return res;
    }
}
