public class FindPerfectSquare {
    private int findLowerBound(int num) {
        int l = 0;
        int r = num;
        int ans = 0;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(mid * mid >= num) {
                ans = mid;
                r = mid - 1;
            } else l = mid + 1;
        }
        return ans;
    }

    private int findUpperBound(int num) {
        int l = 0;
        int r = num;
        int ans = 0;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(mid * mid <= num) {
                ans = mid;
                l = mid + 1;
            } else r = mid -1;
        }
        return ans;
    }

    public int countPerfectSquare(int a, int b) {
        int l = findLowerBound(a);
        int r = findUpperBound(b);
        return (l <= r) ? r - l + 1 : 0;

    }

}
