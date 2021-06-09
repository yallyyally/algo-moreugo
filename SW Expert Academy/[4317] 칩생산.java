import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution{
	static int[][] wapper;
	static int H, W;
	static int ans;
	
	public static boolean isAvailable(int i, int j) {
//		범위 체크
		if(i == H-1 || j == W-1)
			return false;
		System.out.println(i+" "+j);
		if(wapper[i][j] == 1 || wapper[i][j+1] == 1 || wapper[i+1][j] == 1 || wapper[i+1][j+1] == 1)
			return false;
		wapper[i][j] = 1;
		wapper[i][j+1] = 1;
		wapper[i+1][j] = 1;
		wapper[i+1][j+1] = 1;
		return true;
	}
	
//			하나하나 스캔하면서 반도체를 늘려감
	public static void makeChip() {
		for(int i=0; i<H; i++) {
			for(int j=0; j<W; j++) {
				if(isAvailable(i,j)) {
					ans++;
					j++;
				}
					
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		int TC;
		StringBuilder sb = new StringBuilder("");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		TC = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=TC; t++) {
			ans = 0;
//			입력받기
			StringTokenizer st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			wapper = new int[H][W];
			for(int i=0; i<H; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<W; j++) {
					wapper[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			makeChip();
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}
		
//		출력
		System.out.println(sb);
		
	}
}