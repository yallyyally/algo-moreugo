package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

class Main {
	static int N;
	static int cnt; // 조 못정한학생수 (정답)
	static int[] s;
	static boolean[] visited;
	static boolean[] impossible; // 팀원 결성에 실패한 학생을 지목한 학생도 팀원 결성 실패.
	static int[] totalMembers;

	// 팀만들면서 팀 못정한 학생들 cnt ++
	public static void makeTeam() {
		int start = 1;

		while (start <= N) {
			if (!visited[start]) {
				// 소속된 팀이 x -> 조장(출발점)
				int cur = 1;
				int prev = start;
				visited[start] = true;
				totalMembers[start] = cur;
				HashSet<Integer> team = new HashSet<>();
				// 지정한 멤버.
				int member = s[start];
				
				while (member != start) {
					// 다른 팀에 소속 -> 한명도 팀 결성 x
					if (visited[member]) {
						break;
					}
					// 시작점이 아닌 중간지점으로 순회 -> 부분적으로 팀결성
					// 2 3 4 5 3 인 경우 3,4,5 끼리 팀 결성.
					if (team.contains(member)) {
						// 일부 팀 결성 : 마지막까지의 누적합 - 중간지점까지의 누적합 + 1
						cnt += totalMembers[prev] - totalMembers[member] + 1;
						break;
					}
					// 팀에 추가
					team.add(member);
					// 현재 멤버까지 누적 합 기록
					totalMembers[member] = ++cur;
					prev = member;
					member = s[member];
				}
				// 시작점으로 돌아온 경우 -> 팀 결성 완 || 시작점으로 돌아오지 않았는데 종료한 경우 -> 팀 결성 x
				// 팀 결성 완료된 경우 : 끝 멤버의 누적합 - 시작멤버의 누적합 + 1
				if(member == start)
					cnt += totalMembers[prev];
				//결성이 완료했건 실패했건 재방문 x
				for (int person : team) {
					visited[person] = true;
				}
			}
			start++;

		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder("");
		for (int t = 0; t < T; t++) {
			cnt = 0;
			N = Integer.parseInt(br.readLine());
			s = new int[N + 1];
			visited = new boolean[N + 1];
			totalMembers = new int[N + 1];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= N; i++)
				s[i] = Integer.parseInt(st.nextToken());
			makeTeam();
			sb.append(N - cnt).append("\n");
		}
		System.out.println(sb);
	}
}