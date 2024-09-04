import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0];
            int end = commands[i][1];
            int check = commands[i][2];
            
            int[] temp = new int[end - start + 1];
            for (int j = start; j <= end; j++) {
                temp[j - start] = array[j - 1];
            }
            Arrays.sort(temp);
            
            answerList.add(temp[check - 1]);
        }
        
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}