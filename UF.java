public class UF {
    protected int[] id;
    protected int[] count;
    public UF(int N){
        id = new int[N];
        count = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
            count[i] = 1;
        }
    }
    public boolean connected(int p, int q){

        return find(p) == find(q);
    }

    public int find(int p){
        while(p != id[p]){
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }

    public void union(int p, int q){
        int pID = find(p);
        int qID = find(q);

        if(pID == qID){
            return;
        }
        id[qID] = pID;
        count[pID] += count[qID];
    }
}
