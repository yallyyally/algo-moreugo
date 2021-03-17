package webex;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
	static int[][] synergy;
	static int N;
	static int minDist;
	static boolean[] selected;
	
	public static int getCurSynergy(int person, boolean startTeam) {
		int curSynergy = 0;

		for(int i=0; i<N; i++) {
			//같은 팀인 경우 시너지 더하기.
			if(selected[i] == startTeam)
				curSynergy += synergy[person][i];
		}
		
		return curSynergy;
	}
	public static void comb(int cnt, int target) {
		
		if(cnt == N/2) {
			//각 팀의 시너지.
			int startS = 0;
			int linkS = 0;
			for(int i=0; i<N; i++) { //각 팀원마다 시너지 합      
				if(selected[i])
					startS += getCurSynergy(i, selected[i]);
				else
					linkS += getCurSynergy(i, selected[i]);
			}
			
			//최소 차이 업데이트
			if(Math.abs(startS - linkS) < minDist)
				minDist = Math.abs(startS - linkS);
		
			return;
		}
		
		if(target == N) {
			return;
		}
		
		//선택
		selected[target] = true;
		comb(cnt+1, target+1);
		//비선택
		selected[target] = false;
		comb(cnt, target+1);
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		synergy = new int[N][N];
		minDist = Integer.MAX_VALUE;
		selected = new boolean[N];
		
		//시너지 입력받기
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				synergy[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		comb(0, 0);
		System.out.println(minDist);
	}
}