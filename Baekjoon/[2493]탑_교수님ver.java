package day0205;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Test_HW_2493_탑 {
	
	static class Tower{
		int height, num;
		Tower(int h, int n) {
			this.height = h;
			this.num = n;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int topCnt = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		Stack<Tower> stack = new Stack<>();
		for(int i=1; i<=topCnt; i++) {
			int h = Integer.parseInt(st.nextToken());
			//내 왼쪽에 있는데 나보다 작다고 ? 필요 없어! 
			//나보다 높으면 냄겨놓챠
			while(!stack.empty() && stack.peek().height < h) 
				stack.pop();
			//내가 너무 높아서 앞에 애 나감
			if(stack.isEmpty())
				sb.append(0+" ");
			else
				sb.append(stack.peek().num+" ");
			stack.push(new Tower(h, i)); //내가 왼쪽 애보다 작아도 내 오른쪽 애보다 클 수 있으므로 일단 나는 무조건 push - 3 2 1 이 경우.  
			
	}
		System.out.println(sb.toString());
	}

}
