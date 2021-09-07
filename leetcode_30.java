import java.util.*;
public class leetcode_30 {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        LinkedList<String> set = new LinkedList<>();
        for(int i=0; i<words.length; i++){
            set.add(words[i]);
        }
        for(int i=0; i<s.length(); i++){
            if(isMatch(s, i, set)){
                res.add(i);
            }
        }
        return res;
    }
    public boolean isMatch(String s, int start, LinkedList<String> set){
        LinkedList<String> tmp = new LinkedList<>(set);
        int len = tmp.getFirst().length();
        while(tmp.size()>0 && start+len<=s.length()){
            if(tmp.contains(s.substring(start, start+len))){
                tmp.remove(s.substring(start, start+len));
                start+=len;
            }
            else{
                break;
            }
        }
        if(tmp.size()==0)
            return true;
        return false;
    }
}
