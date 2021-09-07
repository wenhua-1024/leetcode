import java.util.*;
public class leetcode_32 {
    public int longestValidParentheses(String s) {
    	int max=0;//存放最大的长度
    	int len=s.length();//字符串长度
    	Stack<Integer> stack=new Stack<Integer>();//暂存字符
    	stack.push(-1);//初始化栈底
    	for(int i=0;i<len;i++) {//遍历字符串
    		if(s.charAt(i)=='(')//字符串存在（
    			stack.push(i);//下标入栈
    		else {//只有右边
    			stack.pop();//下标出栈
    			if(stack.isEmpty()) {//出栈以后，栈为空
    				stack.push(i);//让当前下标进栈
    			}else {//不为空，就计算长度差值
    				max=Math.max(max, i-stack.peek());//选出最长的长度
    			}
    		}
    	}
    	return max;
    }
    
}
