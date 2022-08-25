public class leetcode_853 {
    public static void main(String[] args) {
        
        int target = 10; 
        int[] position = {0,4,2};
        int[] speed = {2,1,3};

        int res = carFleet(target, position, speed);
        System.out.println(res);
    }

    public static int carFleet(int target, int[] position, int[] speed){
        // int max = Integer.MIN_VALUE;
        if(position.length == 0)
            return 0;
        for(int i=0; i<position.length; i++){
            position[i] = target - position[i];
        }
        sort(position, speed, 0, position.length-1);
        // float min = Integer.MIN_VALUE;
        float[] time = new float[position.length];
        for(int i=0; i<position.length; i++){
            time[i] = (float)position[i] / speed[i];
        }
        int ans = 1;
        for(int i=time.length-1; i>0; i--){
            if(time[i] >= time[i-1])
                time[i-1] = time[i];
            else
                ans++;
        }
        return ans;
    }

    public static void sort(int[] arr, int[] speed, int start, int end){
        if(start>=end)
            return;
        int left = start;
        int right = end;
        int tmp = arr[start];
        int tmp_s = speed[start];
        int flag = 1;
        while(left<right){
            if(flag==0){
                if(arr[left]<tmp){
                    arr[right] = arr[left];
                    speed[right] = speed[left];
                    flag=1;
                }
                else
                    left++;
            }
            else if(flag==1){
                if(arr[right]>tmp){
                    arr[left] = arr[right];
                    speed[left] = speed[right];
                    flag=0;
                }
                else{
                    right--;
                }
            } 
        }
        arr[left]=tmp;
        speed[left] = tmp_s;
        sort(arr, speed, start, left-1);
        sort(arr, speed, left + 1, end);
    }
}
