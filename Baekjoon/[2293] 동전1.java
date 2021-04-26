import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
	static int n, k;
	static int[][] dp;
	static int[] coins;
	
	public static void main(String[] args) throws IOException {
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(br.readLine());
		 n = Integer.parseInt(st.nextToken());
		 k = Integer.parseInt(st.nextToken());
		 dp = new int[n+1][k+1];
		 coins = new int[n+1];
		 for(int i=1; i<=n; i++) {
			 coins[i] = Integer.parseInt(br.readLine());
		 }
		 
		 for(int i=1; i<=n; i++) {
//		 coins[i]번째까지만 사용했을 때의 가짓수 저장.
			 dp[i][0] = 1; //하나도 안 낼 때의 경우의 수 -> 여기에 동전을 더 추가할 때 경우의 수를 그대로 가져다 쓰기 위해.
			 for(int j=1; j<=k; j++) {
//				 이전 화폐 단위에 누적.
				 dp[i][j] += dp[i-1][j];
				 if(j - coins[i] >= 0) {
//					 j원을 내는 경우의 수: j-coins[i]원 내고,  coin[i]동전만 추가로 내는 경우
//					 dp[i][0] = 1이므로 coin[i]원을 낼 땐 coin[i]원 동전 하나만 내는 것으로 계산.
					 dp[i][j] += dp[i][j-coins[i]];
				 }
			 }
		 }
		 System.out.println(dp[n][k]);
	}
}