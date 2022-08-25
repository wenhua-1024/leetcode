public class leetcode_1400 {
    public static void main(String[] args) {
        String s = "ibzkwaxxaggkiwjbeysz";
        int k=15;
        boolean res = canConstruct(s, k);
        System.out.println(res);
    }
    public static boolean canConstruct(String s, int k){
        int[] arr = new int[26];
        for(int i=0; i<s.length(); i++){
            arr[s.charAt(i)-'a']++;
        }
        int odd = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i]%2 == 1)
                odd++;
        }
        int min = odd;
        // int max = odd + (s.length()-odd)/2;
        // System.out.println(min);
        // System.out.println(s.length());
        if((k>=min && k<=s.length()))
            return true;
        return false;
    }
}
