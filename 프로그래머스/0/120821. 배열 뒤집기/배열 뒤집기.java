class Solution {
    public int[] solution(int[] num_list) {
        
        int N = num_list.length;
        
        int[] result = new int[N];
        
        for (int i = N-1; i >= 0; i--) {
            result[N-i-1] = num_list[i];
        }
                
        return result;
    }
}