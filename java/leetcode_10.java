public class leetcode_10 {
    public boolean isMatch(String s, String p) {
        if(s.length() == 0 && p.length() == 0)
            return true;
        else if(s.length() == 0 || p.length() == 0)
            return false;
        
        int index_p = 0;
        int index_s = 0;
        char c = ' ';
        while(index_p < p.length() && index_s < s.length()){
            if(p.charAt(index_p) == '.'){
                c = p.charAt(index_p);
                index_p++;
                index_s++;      
            }
            else if(p.charAt(index_p) == '*' && ('.' == c || s.charAt(index_s) == c)){
                index_s++;
            }
            else if(p.charAt(index_p) == '*' && s.charAt(index_s) != c){
                index_p++;
            }
            else if(p.charAt(index_p) == s.charAt(index_s))
            {
                c = p.charAt(index_p);
                index_s++;
                index_p++;
            }
            else if(p.charAt(index_p) != s.charAt(index_s) && (p.charAt(index_p)==c) || (index_p<p.length()-1 && p.charAt(++index_p) == '*')){
                index_p++;
            }
            else{
                return false;
            }
        }
        while(index_p < p.length()){
            if(p.charAt(index_p) == '*' || c == p.charAt(index_p)){
                index_p++;
            }
            else{
                break;
            }
        }
        if(index_p == p.length() && index_s == s.length()){
            return true;
        }
        else{
            return false;
        }
    }
}
