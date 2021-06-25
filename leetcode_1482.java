public class leetcode_1482 {
    public int minDays(int[] bloomDay, int m, int k){
        if(m>bloomDay.length/k)
            return -1;
        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;
        for(int i=0; i<bloomDay.length; i++){
            low = Math.min(low, bloomDay[i]);
            high = Math.max(high, bloomDay[i]);
        }
        while(low<high){
            int day = (high-low)/2 + low;
            if(canMake(bloomDay, day, m, k)){
                high = day;
            }else{
                low = day+1;
            }
        }
        return low;
    }
    // 判断制定天数是否能完成任务
    private boolean canMake(int[] bloomDay, int day, int m, int k){
        int counts = 0;
        int flowers = 0;
        for(int i=0; i<bloomDay.length && counts<m; i++){
            if(bloomDay[i]<=day){
                flowers++;
                if(flowers>=k){
                    counts++;
                    flowers=0;
                }
            }else{
                flowers=0;
            }
        }
        return counts>=m;
    }
}
