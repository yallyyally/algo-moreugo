package webex;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	
	static long[] height;
	static int N, M;
	static long B;
	static long minTime = Long.MAX_VALUE;
	static long maxHeight = -1;

	// curHeight에 맞춰서 집터를 깎는다.
	// 이 때, height는 크기순으로 정렬 되있으므로 현재 블록수가 모자라면 다음에도 모자랄 것ㄱ이므로 바로 break 해준다.
	public static void makeHouseGround(long curHeight) {

//		System.out.println("현재 높이 "+curHeight);
		long curTime = 0;
		long blockInventory = B; // 현재 인벤토리에 있는 블록
		long blocks; // 빼주거나 더해줄 블록

		for (long h : height) {
			// 클 때 -> 깎기
			if (h > curHeight) {
				blocks = h - curHeight;
				// 시간 소요, 인벤토리에 블록 증가.
				curTime += 2 * blocks;
				blockInventory += blocks;
			}
			// 작을 때 ->block 쌓기
			// 같을때는 그냥 지나감.(시간 0초 소요)
			else if (h < curHeight) {
				blocks = curHeight - h;
				// 블록 있나 확인
				if (blockInventory >= blocks) {
					curTime += blocks;
					blockInventory -= blocks;
				} else // 블록 없으면 불가.
					return;
			}
		}

		// 시간, 길이 업데이트 -> curHeight를 main에서 점차 감소시키고 있기 때문에 
		// 시간이 같을 땐 고려 안해줘도 ㄱㅊ (어차피 이전 높이보다 작은 값이라 비교할 필요 없음)
		if (curTime < minTime) {
			minTime = curTime;
			maxHeight = curHeight;
		}
	}

	public static void reverseArray() {
		int len = N * M;
		long tmp;
		for (int i = 0; i < len / 2; i++) {
			tmp = height[i];
			height[i] = height[len - 1 - i];
			height[len - 1 - i] = tmp;
		}
//		for (int i = 0; i < N * M; i++)
//			System.out.println(height[i]);

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		B = Long.parseLong(st.nextToken());
		height = new long[N * M];

		int idx = 0;
		long input;

		long min = Long.MAX_VALUE;
		long max = -1;
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				input = Long.parseLong(st.nextToken());
				height[idx++] = input;
				if(input > max)
					max = input;
				if(input < min)
					min = input;
			}
		}

		// 크기 내림차순 정렬 ->block 수가 모자라면 바로 break 하기 위함.
		Arrays.sort(height);
		reverseArray();

		// 각 길이에 맞춰서 자르기 -> 최소 시간과 그 때의 길이(최대) 업데이트.
		for(long i=max; i>=min; i--) {
			makeHouseGround(i);
		}

		// 출력
		System.out.println(minTime + " " + maxHeight);
	}
}