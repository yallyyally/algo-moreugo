import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
	static long[] arr;
	static int N, R;
	static int P = 1234567891;

	public static long power(long num, long times) {
	    if( times == 1 ) return num;
	    long cur = power(num, times/2);
	    long res = times % 2 == 1 ? cur * cur % P * num % P : cur * cur % P;
	    return res;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new long[1000001];
		arr[0] = 1;
		for(int i=1; i<=1000000; i++) {
			arr[i] = arr[i-1] * i % P;
		}
		int TC = Integer.parseInt(br.readLine());
		long res;
		StringBuilder sb = new StringBuilder("");
		for (int t = 1; t <= TC; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			R= Integer.parseInt(st.nextToken());
			res =  arr[N] * power((arr[N-R] * arr[R]) % P, P-2) % P;
			sb.append("#").append(t).append(" ").append(res).append("\n");
		}
		System.out.println(sb);
	}

}
