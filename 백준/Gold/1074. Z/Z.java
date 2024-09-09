import java.util.Scanner;

public class Main {
    static int count = 0;  // 순서를 저장할 변수
    static int r, c;       // 찾고자 하는 좌표
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();  // N은 2^N 크기의 행렬을 의미
        r = sc.nextInt();      // 찾고자 하는 행 좌표
        c = sc.nextInt();      // 찾고자 하는 열 좌표
        
        // 행렬 크기는 2^N x 2^N
        int size = (int)Math.pow(2, N);
        
        // 분할 정복 시작
        solve(size, 0, 0);
        System.out.print(count);
    }
    
    // 분할 정복 함수
    static void solve(int size, int row, int col) {
        if (size == 1) {
            return;
        }
        
        // 행렬을 4개의 영역으로 나눔
        int newSize = size / 2;
        
        // 1사분면 (왼쪽 위)
        if (r < row + newSize && c < col + newSize) {
            solve(newSize, row, col);
        }
        // 2사분면 (오른쪽 위)
        else if (r < row + newSize && c >= col + newSize) {
            count += newSize * newSize;  // 1사분면 탐색을 건너뛰므로 순번 추가
            solve(newSize, row, col + newSize);
        }
        // 3사분면 (왼쪽 아래)
        else if (r >= row + newSize && c < col + newSize) {
            count += 2 * newSize * newSize;  // 1, 2사분면 탐색을 건너뛰므로 순번 추가
            solve(newSize, row + newSize, col);
        }
        // 4사분면 (오른쪽 아래)
        else {
            count += 3 * newSize * newSize;  // 1, 2, 3사분면 탐색을 건너뛰므로 순번 추가
            solve(newSize, row + newSize, col + newSize);
        }
    }
}
