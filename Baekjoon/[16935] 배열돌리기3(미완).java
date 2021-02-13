package webex;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static char[][] origin;
	static char[][] moved;
	static int height, width;
	static int[] limitX = new int[4];
	static int[] limitY = new int[4];
	static int[] plusX = new int[4];
	static int[] plusY = new int[4];

	// 상하반전
	public static void upsideDown() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[height - 1 - i][j] = origin[i][j];
			}
		}
	}

	// 좌우반전
	public static void flipLeftRight() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[i][width - 1 - j] = origin[i][j];
			}
		}
	}

	// height, width 변경
	public static void swapHeightWidth() {
		int temp = height;
		height = width;
		width = temp;
	}

	// 오른쪽으로 90 --> height, width 바뀜에 유의.
	public static void rotateRight() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[j][height - 1 - i] = origin[i][j];
			}
		}
		swapHeightWidth();
	}

	// 왼쪽으로 90
	public static void rotateLeft() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[width - 1 - j][i] = origin[i][j];
			}
		}
		swapHeightWidth();
	}

	public static void moveClockWise() {
		int startX = 0;
		int startY = 0;
		// height, width가 여러번 바뀔것이므로 여기서 세팅함.
		limitX[0] = height / 2;
		limitX[1] = height / 2;
		limitX[2] = height;
		limitX[3] = height;

		limitY[0] = width / 2;
		limitY[1] = width;
		limitY[2] = width;
		limitY[3] = width / 2;

		plusX[0] = 0;
		plusX[1] = height / 2;
		plusX[2] = 0;
		plusX[3] = -height / 2;

		plusY[0] = width / 2;
		plusY[1] = 0;
		plusY[2] = -width / 2;
		plusY[3] = 0;

		for (int k = 0; k < 4; k++) { // 네 그룹
			for (int i = startX; i < limitX[k]; i++) {
				for (int j = startY; j < limitY[k]; j++) {
					moved[i + plusX[k]][j + plusY[k]] = origin[i][j];
				}
			}
			startX += plusX[k];
			startY += plusY[k];
		}
	}

	// 시계 반대방향으로 이동
	public static void moveCounterClockWise() {
		int startX = 0;
		int startY = 0;
		// height, width가 여러번 바뀔것이므로 여기서 세팅함.
		limitX[0] = height / 2;
		limitX[1] = height;
		limitX[2] = height;
		limitX[3] = height / 2;

		limitY[0] = width / 2;
		limitY[1] = width / 2;
		limitY[2] = width;
		limitY[3] = width;

		plusX[0] = height / 2;
		plusX[1] = 0;
		plusX[2] = -height / 2;
		plusX[3] = 0;

		plusY[0] = 0;
		plusY[1] = width / 2;
		plusY[2] = 0;
		plusY[3] = -width / 2;

		for (int k = 0; k < 4; k++) { // 네 그룹
			for (int i = startX; i < limitX[k]; i++) {
				for (int j = startY; j < limitY[k]; j++) {
					moved[i + plusX[k]][j + plusY[k]] = origin[i][j];
				}
			}
			startX += plusX[k];
			startY += plusY[k];
		}
	}

	// moved를 origin에 복사.
	public static void copyToOrigin() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				origin[i][j] = moved[i][j];
			}
		}
	}

	// origin 출력
	public static void printResult() {
		// 연산 크기가 바뀌었을지도 모르므로.
		StringBuilder sb;
		for (int i = 0; i < height; i++) {
			sb = new StringBuilder("");
			for (int j = 0; j < width; j++) {
				sb.append(origin[i][j]).append(" ");
			} // 한줄씩 출력
//			sb.setLength(sb.length()-1);
			System.out.println(sb.toString());
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String inputLine;
		int R;
		// N, M, R 입력
		N = Integer.parseInt(st.nextToken());
		height = N;
		M = Integer.parseInt(st.nextToken());
		width = M;
		R = Integer.parseInt(st.nextToken());
		// 배열 입력 >>최대한 크게
		origin = N>=M ? new char[N][N] : new char [M][M];
		moved = N>=M ? new char[N][N] : new char [M][M];
		for (int i = 0; i < height; i++) {
			inputLine = br.readLine();
			int k = 0;
			for (int j = 0; j < width * 2; j += 2) {
				origin[i][k++] = inputLine.charAt(j);
			}
		}
		// 연산 종류
		String kinds = br.readLine();
		char kind;
		// 연산 시행
			for (int c = 0; c < R*2; c += 2) {
				kind = kinds.charAt(c);
				switch (kind) {
				case '1': // 상하
					upsideDown();
					break;
				case '2': // 좌우
					flipLeftRight();
					break;
				case '3':// 오른쪽 09
					rotateRight();
					break;
				case '4':
					rotateLeft();
					break;
				case '5':
					moveClockWise();
					break;
				case '6':
					moveCounterClockWise();

				}
				// origin에 moved 복사
				copyToOrigin();
				printResult();
				System.out.println();
			}
		// 연산 출력
		printResult();
	}
}
