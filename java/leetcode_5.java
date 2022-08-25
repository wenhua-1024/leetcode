public class leetcode_5 {
    private String str;
    public String longestPalindrome(String s) {
        str = "";
        for(int i=0; i<s.length(); i++){
            findPalindrome(s, i, "odd");
            findPalindrome(s, i, "even");
        }
        return str;

    }
    public void findPalindrome(String s, int start, String flag){
        int left = start;
        int right = start;
        if(!flag.equals("odd")){
            right = start+1;
        }
        while(left>=0 && right<s.length()){
            if(s.charAt(left) == s.charAt(right)){
                left--;
                right++;
            }
            else{
                if(str.length()<(right-left-1)){
                    str = s.substring(left+1, right);
                }
                return;
            }
        }
        if(str.length()<(right-left-1)){
            str = s.substring(left+1, right);
        }
    }
}
