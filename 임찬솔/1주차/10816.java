import java.util.Scanner;
import java.util.Arrays;
import java.util.StringTokenizer;     //stringbulider사용하기 위해

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr= new int[N];//N개 길이의 배열 생성

        for(int i=0; i<N; i++)
            arr[i] = sc.nextInt();

        Arrays.sort(arr);    //이분탐색 쓰려면 정렬 필수

        int M = sc.nextInt();
        int value=0;
        StringBuilder sb = new StringBuilder();     //여러개의 문자열을 관리할때 사용하면 편리한 stringbuilder 클래스 ( M길이 배열을 하나 더 생성하면 시간초과 됨)
        
        
        for(int k=0; k<M; k++){
            value = sc.nextInt();     //값을 받자마자
            sb.append(upperBound(arr, value) - lowerBound(arr, value)).append(" ");   //upperbound-lowerbound의 차이가 value값의 개수임을 이용하여 바로 sb객체에 추가

        }
            System.out.print(sb);


    }

    public static int lowerBound(int[] arr,  int value) {
        int low = 0;
        int high = arr.length;
        while (low < high) {
            final int mid = low + (high - low)/2;
            if (value <= arr[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    
    /*첫번째 불변식은 low-1<high, 두번째 불변식은 arr[low-1]<value<=arr[high]이다.
    while문의 조건이 low<high이므로 첫번째 불변식은 자명하고, value<=arr[mid]일 때 mid 는 high이므로 value<=arr[high]이고,
    value>arr[mid]일 경우 low-1 = mid 이므로 value>arr[low-1]이다.
    반복문을 탈출할때에는 low>=high이고, 불변식이 low-1<high이므로 low==high가 된다.
    불변식이 성립한다고 가정하면 arr[low-1]<value<=arr[low]이므로 arr[low]가 우리가 원하는 값임을 알 수 있다.
    */
    
    public static int upperBound(int[] arr, int value) {
        int low = 0;
        int high = arr.length;
        while (low < high) {
            final int mid = low + (high - low)/2;
            if (value >= arr[mid]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    /*위의 lowerbound와 유사하게 첫번째 불변식은 low-1<high, 두번째 불변식은 arr[low-1]<=value<arr[high]이다.
    while문의 조건이 low<high이므로 첫번째 불변식은 자명하고, value>=arr[mid]일 때 mid 는 low-1이므로 value>=arr[low-1]이고,
    value<arr[mid]일 경우 high = mid 이므로 value<arr[high]이다.
    반복문을 탈출할때에는 low>=high이고, 불변식이 low-1<high이므로 low==high가 된다.
    불변식이 성립한다고 가정하면 arr[low-1]<value<=arr[low]이므로 arr[low]가 우리가 원하는 값임을 알 수 있다.
    */

}
