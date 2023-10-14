import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] visited;
    static List<List<Character>> arr;
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str, " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();

        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String tiles = br.readLine();

            List<Character> tile = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                tile.add(j, tiles.charAt(j));
            }
            arr.add(i, tile);
        }

        int count = 0;

        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < M; j++) {
                if(visited[i][j]) continue;
                if(arr.get(i).get(j) == '-') DFS(i, j, false);
                else DFS(i, j, true);
                count++;
            }
        }

        System.out.print(count);
    }

    private static void DFS(int i, int j, boolean row) {
        visited[i][j] = true;
        if(row) {
            i++;
            if(i<N && arr.get(i).get(j) != '-') DFS(i, j, true);
        } else {
            j++;
            if(j<M && arr.get(i).get(j) == '-') DFS(i, j, false);
        }
    }
}
