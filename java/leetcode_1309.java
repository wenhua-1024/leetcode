public class leetcode_1309 {
    public static void main(String[] args) {
        String s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#";
        String res = freqAlphabets(s);
        System.out.println(res);
    }
    public static String freqAlphabets(String s){
        StringBuffer buffer = new StringBuffer();
        for(int i=0; i<s.length(); i++){
            int num = 0;
            if(i+2<s.length() && s.charAt(i+2) == '#'){
                num += s.charAt(i)-'0';
                num = num*10 + s.charAt(i+1) - '0';
                i++;
                i++;
            }
            else
                num = s.charAt(i)-'0';
            buffer.append((char)('a'+num-1));
        }
        return buffer.toString();
    }
}
