import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        
        int N = numbers.length;
        
        String[] temp = new String[N];
        
        for (int i = 0; i < N; i++) {
            temp[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(temp, (str1, str2) -> (str2 + str1).compareTo(str1 + str2));
                
        StringBuilder answer = new StringBuilder();
        
        for (String str : temp) {
            answer.append(str);
        }
        
        if (answer.charAt(0) == '0') {
            answer = new StringBuilder("0");
        }
        
        return answer.toString();
    }
}