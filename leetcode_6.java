public class leetcode_6 {
    public String convert(String s, int numRows) {
        int step = 2*numRows-2;
        if(step==0)
            return s;
        StringBuffer res = new StringBuffer();
        for(int i=0; i<numRows; i++){
            
            if(i == 0 || i == numRows-1){
                int index = i;
                while(index<s.length()){
                    res.append(s.charAt(index));
                    index += step;
                }
            }
            else{
                int index = i;
                while(index<s.length()){
                    res.append(s.charAt(index));
                    if(index+ (step-2*i) < s.length()){
                        res.append(s.charAt(index+(step-2*i)));
                    }
                    index += step;
                }
            }
        } 
        return res.toString();
    }
}
