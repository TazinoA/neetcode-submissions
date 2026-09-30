class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int l = 0; l<n; l++){
            nums1[m] = nums2[l];
            m++;
        }
        Arrays.sort(nums1);
    }
}