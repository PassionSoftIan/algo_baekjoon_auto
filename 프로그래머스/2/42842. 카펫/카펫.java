/*

1. 중앙은 노란색
2. 테두리 1줄은 갈색
3. 노란색 개수, 갈색 개수 주어짐.
4. 8 <= 갈색 <= 5000
5. 1 <= 노란색 <= 2000000
6. 세로 <= 가로

*/

import java.util.*;

class Solution {
    
    public static int area;
    
    public static int [] answer = new int[2];
    
    public int[] solution(int brown, int yellow) {
        
        area = brown + yellow;
                
        for (int col = 3; col <= area/3; col++) {
            if (area % col != 0 ) {
                continue;
            }
            int row = area / col;
            if (row <= col && ((row - 2) * (col -2) == yellow)) {
                answer[0] = col;
                answer[1] = row;
            }
        }        
        return answer;
    }
}