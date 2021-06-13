import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

class Solution {
//	쿼리 - 점수 목록
	static HashMap<String, int[]> map;
	static HashMap<String, Integer> idxMap; // int[] 배열의 인덱스 관리

	static int infoLen;

	public static void updateScoreArr(String info, int score) {
		int[] arr;
		int idx;
//		배열 생성
		if (map.get(info) == null) {
			map.put(info, new int[infoLen]);
			idxMap.put(info, 0);
		}
		
		arr = map.get(info);
		idx = idxMap.get(info);

//		배열에 점수 넣어주고, 인덱스 증가
		arr[idx] = score;
		idxMap.put(info, idx + 1);
	}

	public static void insertKey(String lang, String field, String experience, String food, int score) {
		
		updateScoreArr(lang+field+experience+food,score);
		updateScoreArr("-"+field+experience+food,score);
		updateScoreArr(lang+"-"+experience+food,score);
		updateScoreArr(lang+field+"-"+food,score);
		updateScoreArr(lang+field+experience+"-",score);
		updateScoreArr("--"+experience+food,score);
		updateScoreArr("-"+field+"-"+food,score);
		updateScoreArr("-"+field+experience+"-",score);
		updateScoreArr(lang+"--"+food,score);
		updateScoreArr(lang+"-"+experience+"-",score);
		updateScoreArr(lang+field+"--",score);
		updateScoreArr("---"+food,score);
		updateScoreArr("--"+experience+"-",score);
		updateScoreArr("-"+field+"--",score);
		updateScoreArr(lang+"---",score);
		updateScoreArr("----",score);

	}
	
//	특정 점수 이상 사람 수 반환
	public int getResult(String key, int score) {
		if(map.get(key) == null)
			return 0;
		int[] arr = Arrays.copyOfRange(map.get(key), 0, idxMap.get(key));
		
		int start = 0;
		int end = arr.length - 1;
		int res = 0;
//		일단 정렬
		Arrays.sort(arr);
		
		while(start <= end) {
			int middle = (start + end) / 2;
			if(arr[middle] < score)
				start = middle + 1;
			else {
				res = end - start + 1;
				end = middle - 1;
			}
		}
		
		return res;
		
	}
	public int selectQuery(String lang, String field, String experience, String food, int score) {
		int result = 0;
		result += getResult(lang+field+experience+food,score);
		return result;
	}
	
	public int[] solution(String[] info, String[] query) {
		StringTokenizer st;
		map = new HashMap<>();
		idxMap = new HashMap<>();

		infoLen = info.length;
		int queryLen = query.length;
		int[] answer = new int[queryLen];

//    	지원자 정보 파싱 -> 해쉬맵에 저장.
		for (int i = 0; i < infoLen; i++) {
			st = new StringTokenizer(info[i]);
//			지원자의 정보에 따라 해당하는 쿼리를 맵에 key 값으로 넣는다
//			- 위치는 현재 언어/분야/경력/음식에 따라 4C4+4C3+4C2+4C1 = 15가지 
//			+) -가 하나도 없는 본래 정보 한가지 => 총 16가지
			String lang = st.nextToken();
			String field = st.nextToken();
			String experience = st.nextToken();
			String food = st.nextToken();
			int score = Integer.parseInt(st.nextToken());
			insertKey(lang, field, experience, food, score);

		}
		
		
//		쿼리 파싱
		for (int q = 0; q < queryLen; q++) {
//        	stringTokenizer 쓰면 delim을 쪼개서 문자 기준으로 분리하더라
			String[] tokens = query[q].split(" and ");
//        	마지막은 and가 없어서 pizza 150 이렇게 나옴
			st = new StringTokenizer(tokens[3]);
			answer[q] = selectQuery(tokens[0], tokens[1], tokens[2], st.nextToken(), Integer.parseInt(st.nextToken()));
		}

		return answer;
	}


}