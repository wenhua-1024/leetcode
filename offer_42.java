public class offer_42 {
    public static void main(String[] args) {
        int[] nums = {-2,1};
        int res = maxSubArray(nums);
        System.out.println(res);
    }
    
    public static int maxSubArray(int[] nums){
        if(nums.length == 0)
            return 0;
        int max = Integer.MIN_VALUE;
        int ans = 0;
        for(int i=0; i<nums.length; i++){
            ans += nums[i];
            max = Math.max(ans, max);
            if(ans<0) ans=0;
        }
        return max;
    }
}
