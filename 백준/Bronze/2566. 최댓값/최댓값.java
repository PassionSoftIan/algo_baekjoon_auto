import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = 9;
        int M = 9;

        int max = 0;
        int row = 0;
        int col = 0;

        ArrayList<Integer> result = new ArrayList<>();

        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str, " ");
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (max < num) {
                    max = num;
                    row = i;
                    col = j;
                }
            }
        }
        result.add(row+1);
        result.add(col+1);
        System.out.println(max);

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
