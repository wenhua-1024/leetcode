public class leetcode_275 {
    public static void main(String[] args) {
        int[] citations = {99, 100};
        int res = hIndex(citations);
        System.out.println(res);
    }
    public static int hIndex(int[] citations){
        // 使用二分法进行查找
        int res = findHIndex(citations, 0, citations.length-1);
        return res;
    }

    private static int findHIndex(int[] arr, int start, int end){
        if(start>=end)
            return Math.min(arr.length - start, arr[start]);
        int len = arr.length;
        int left = start;
        int right = end;
        int mid = (right-left)/2 + left;
        if(arr[mid] < len-mid){
            return findHIndex(arr, mid+1, end);
        }
        return findHIndex(arr, start, mid);
    }
}
