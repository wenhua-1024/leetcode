public class leetcode_2 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] res = new int[m+n];
        int index = 0;
        int index1 = 0;
        int index2 = 0;
        while(index<res.length){
            if(index1<m && index2<n && (nums1[index1] < nums2[index2]) || index2>=n){
                res[index] = nums1[index1];
                index++;
                index1++;
            }
            else{
                res[index] = nums2[index2];
                index++;
                index2++;
            }    
        }
        if(res.length % 2 == 1){
            int mid = (res.length+1)/2;
            return res[mid-1];
        }
        else{
            int mid = (res.length+1)/2;
            return (res[mid-1] + res[mid])/2.0;
        }
    }
}

