import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        
        long[][] DP = new long[N-1][21];
        
        DP[0][numbers[0]] = 1;
        
        for (int i = 1; i < N-1; i++) {
            for (int j = 0; j < 21; j++) {
                if (0 < DP[i-1][j]) {
                    if (0 <= j + numbers[i] && j + numbers[i] <= 20) {
                        DP[i][j + numbers[i]] += DP[i-1][j];
                    }
                    if (0 <= j - numbers[i] && j - numbers[i] <= 20) {
                        DP[i][j - numbers[i]] += DP[i-1][j];
                    }
                }
            }
        }
        System.out.print(DP[N-2][numbers[N-1]]);
        
        
    }
}