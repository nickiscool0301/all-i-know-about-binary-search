public class Main {
    public static void main(String[] args) {
        BinarySearch binarySearch = new BinarySearch();
        int[] arr = {1,4,4,4,4,5,10,20};
        System.out.print("Insertion position for target is: ");
        System.out.println(binarySearch.binarySearchInsertionPosition(arr,2));
        System.out.print("Left most position for target is: ");
        System.out.println(binarySearch.leftMostBinarySearch(arr,4));
        System.out.print("Right most position for target is: ");
        System.out.println(binarySearch.rightMostBinarySearch(arr,4));
        System.out.println(new FindPerfectSquare().countPerfectSquare(9, 24));
    }
}
