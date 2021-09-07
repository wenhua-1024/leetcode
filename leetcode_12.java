public class leetcode_12 {
    StringBuffer res = new StringBuffer();
    String str = "MDCLXVI";
    
    public String intToRoman(int num) {
        int[] arr = {1000, 500, 100, 50, 10, 5, 1};
        for(int i=0; i<str.length(); i++){
            num = OneTpRoman(num, arr, i);
        }
        return res.toString();
    }
    public int OneTpRoman(int num, int[] arr, int index){
        if(index+1<str.length()&& index-1>=0 && num/arr[index+1]>0 && 
        (str.charAt(index+1) == 'I' || str.charAt(index+1) == 'X' || str.charAt(index+1) == 'C')){
            int tmp = num/arr[index+1];
            if(tmp==9){
                res.append(str.charAt(index+1));
                res.append(str.charAt(index-1));
                return num%arr[index+1];
            }
            else if(tmp==4){
                res.append(str.charAt(index+1));
                res.append(str.charAt(index));
                return num%arr[index+1];
            }
        }
        int tmp= num/arr[index];
        for(int i=0; i<tmp; i++){
            res.append(str.charAt(index));
        }
        return num%arr[index];
    }
}
