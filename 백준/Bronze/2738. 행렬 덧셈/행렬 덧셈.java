import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 번째 라인에서 N과 M을 읽어옴
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // N x M 크기의 2차원 배열 생성 및 초기화
        int[][] arr = new int[N][M];

        // 입력 데이터를 배열에 더해줌
        for (int p = 0; p < 2; p++) {
            for (int i = 0; i < N; i++) {
                str = br.readLine();
                st = new StringTokenizer(str, " ");
                for (int j = 0; j < M; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    arr[i][j] += num;
                }
            }
        }

        // 배열을 출력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}