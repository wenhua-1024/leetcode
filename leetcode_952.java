import java.util.HashMap;

public class leetcode_952 {
    public int largestComponentSize(int[] nums) {
        int max = Integer.MIN_VALUE;
        for(int a : nums)
            max = Math.max(max, a);
        
        DSU dsu = new DSU(max+1);
        for(int a : nums){
            for(int k=2; k<=Math.sqrt(a); k++){
                if(a%k == 0){
                    dsu.union(a, k);
                    dsu.union(a, a/k);
                }
            }
        }

        HashMap<Integer, Integer> map = new HashMap<>();

        int ans = 1;
        for(int a : nums){
            int temp = map.getOrDefault(dsu.find(a), 0) +1;
            ans = Math.max(ans, temp);
            // ans += temp;
            map.put(dsu.find(a), temp);
        }
        return ans;
    }

    // 构建并查集
    private class DSU{
        public int[] parent;

        public DSU(int n){
            parent = new int[n];
            for(int i=0; i<n; i++)
                parent[i] = i;
        }

        public int find(int x){
            if(parent[x]!=x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        public void union(int x, int y){
            parent[find(x)] = parent[find(y)];
        }

    }
}
