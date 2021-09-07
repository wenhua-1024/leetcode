public class quickSort {
    public static void main(String[] args) {
        int[] arr = {4,6,8,2,3,10, 20, 10, 3,5,9,0,1,7};
        sort(arr, 0, arr.length-1);
        for(int i=0; i<arr.length; i++){
            System.out.print(arr[i]);
            System.out.print("\t");
        }
    }

    public static void sort(int[] arr, int start, int end){
        if(start>=end)
            return;
        int left = start;
        int right = end;
        int tmp = arr[start];
        int flag = 1;
        while(left<right){
            if(flag==0){
                if(arr[left]>tmp){
                    arr[right] = arr[left];
                    flag=1;
                }
                else
                    left++;
            }
            else if(flag==1){
                if(arr[right]<tmp){
                    arr[left] = arr[right];
                    flag=0;
                }
                else{
                    right--;
                }
            } 
        }
        arr[left]=tmp;
        sort(arr, start, left-1);
        sort(arr, left + 1, end);
    }
}
