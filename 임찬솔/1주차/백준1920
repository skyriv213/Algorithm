import java.util.Scanner;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
        
    Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr= new int[N];//N개 길이의 배열 생성
        
        for(int i=0; i<N; i++)
            arr[i] = sc.nextInt();    
        
        Arrays.sort(arr);    //이분탐색 쓰려면 정렬 필수
        
        int M = sc.nextInt();
        int[] arr2 = new int[M];    //M개 길이의 배열 생성
        
        for(int i=0;i<M; i++)
            arr2[i] = sc.nextInt();
        
        for(int k=0; k<M; k++){
            
            int tmp=binarySearch(arr,arr2[k]);    //이진탐색
        
            if(tmp>=0)        //index값이 0 이상(원하는 값이 존재할 경우)
                System.out.println("1");
            else
                System.out.println("0");
        }
    }
    
  public static int binarySearch(int[] arr, int key) {
 
		int lo = 0;					// 탐색 범위의 왼쪽 끝 인덱스
		int hi = arr.length - 1;	// 탐색 범위의 오른쪽 끝 인덱스
 
		// lo가 hi보다 커지기 전까지 반복한다.
		while(lo <= hi) {
 
			int mid = (lo + hi) / 2;	// 중간위치를 구한다.
 
			// key값이 중간 위치의 값보다 작을 경우
			if(key < arr[mid]) {
				hi = mid - 1;
			}
			// key값이 중간 위치의 값보다 클 경우
			else if(key > arr[mid]) {
				lo = mid + 1;
			}
			// key값과 중간 위치의 값이 같을 경우
			else {
				return mid;
			}
		}
 
		// 찾고자 하는 값이 존재하지 않을 경우
		return -1;
 
	}
}
