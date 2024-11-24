/*
This class contains every implementation and application for binary search
1. binarySearchInsertionPosition
- This method return index equal to target, or the position where the target should be inserted to arr if it does not exist

=> In some case, array can contain a lot of target inside. We can try to find left most, and right most, or maybe the middle
2. leftMostBinarySearch
3. rightMostBinarySearch
4. middleBinarySearch

 */
public class BinarySearch {
    // return left here is because after the loop, left > right.
    public int binarySearchInsertionPosition(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            }
            if (arr[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public int leftMostBinarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        int res = -1;
        while(left <= right) {
            int mid = left + (right - left)/2;
            if(arr[mid] >= target) {
                right = mid -1;
            } else {
                left = mid + 1;
            }
            if(arr[mid] == target) {
                res = mid;
            }
        }
        return res;
    }

    public int rightMostBinarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        int res = -1;
        while(left <= right) {
            int mid = left + (right - left)/2;
            if(arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
            if(arr[mid] == target) {
                res = mid;
            }
        }
        return res;
    }

}
