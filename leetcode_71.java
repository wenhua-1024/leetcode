import java.util.Stack;

public class leetcode_71 {

    public static void main(String[] args) {
        String path = "/a//b////c/d//././/..";
        String res = simplifyPath(path);
        System.out.println(res);
    }

    private static String simplifyPath(String path){
        Stack<String> stack = new Stack<>();
        StringBuffer dir = new StringBuffer();
        for(int i=0; i<path.length(); i++){
            if(path.charAt(i) == '/'){
                if(dir.toString().equals("..")){
                    if(!stack.isEmpty())
                        stack.pop();
                }
                else if(!dir.toString().equals(".") && dir.length()>0){
                    stack.push(dir.toString());
                }    
                dir.setLength(0);
            }
            else
                dir.append(path.charAt(i));
        }
        if(dir.length()>0){
            if(dir.toString().equals("..")){
                if(!stack.isEmpty())
                    stack.pop();
            }
            else if(!dir.toString().equals(".") && dir.length()>0){
                stack.push(dir.toString());
            }
        }
        dir.setLength(0);
        if(stack.isEmpty())
            dir.append("/");
        while(!stack.isEmpty()){
            StringBuffer dic = new StringBuffer("/" + stack.pop());
            dir = dic.append(dir);
        }
        return dir.toString();
    }
}
