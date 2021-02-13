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

	// ���Ϲ���
	public static void upsideDown() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[height - 1 - i][j] = origin[i][j];
			}
		}
	}

	// �¿����
	public static void flipLeftRight() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[i][width - 1 - j] = origin[i][j];
			}
		}
	}

	// height, width ����
	public static void swapHeightWidth() {
		int temp = height;
		height = width;
		width = temp;
	}

	// ���������� 90 --> height, width �ٲ� ����.
	public static void rotateRight() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				moved[j][height - 1 - i] = origin[i][j];
			}
		}
		swapHeightWidth();
	}

	// �������� 90
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
		// height, width�� ������ �ٲ���̹Ƿ� ���⼭ ������.
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

		for (int k = 0; k < 4; k++) { // �� �׷�
			for (int i = startX; i < limitX[k]; i++) {
				for (int j = startY; j < limitY[k]; j++) {
					moved[i + plusX[k]][j + plusY[k]] = origin[i][j];
				}
			}
			startX += plusX[k];
			startY += plusY[k];
		}
	}

	// �ð� �ݴ�������� �̵�
	public static void moveCounterClockWise() {
		int startX = 0;
		int startY = 0;
		// height, width�� ������ �ٲ���̹Ƿ� ���⼭ ������.
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

		for (int k = 0; k < 4; k++) { // �� �׷�
			for (int i = startX; i < limitX[k]; i++) {
				for (int j = startY; j < limitY[k]; j++) {
					moved[i + plusX[k]][j + plusY[k]] = origin[i][j];
				}
			}
			startX += plusX[k];
			startY += plusY[k];
		}
	}

	// moved�� origin�� ����.
	public static void copyToOrigin() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				origin[i][j] = moved[i][j];
			}
		}
	}

	// origin ���
	public static void printResult() {
		// ���� ũ�Ⱑ �ٲ�������� �𸣹Ƿ�.
		StringBuilder sb;
		for (int i = 0; i < height; i++) {
			sb = new StringBuilder("");
			for (int j = 0; j < width; j++) {
				sb.append(origin[i][j]).append(" ");
			} // ���پ� ���
//			sb.setLength(sb.length()-1);
			System.out.println(sb.toString());
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String inputLine;
		int R;
		// N, M, R �Է�
		N = Integer.parseInt(st.nextToken());
		height = N;
		M = Integer.parseInt(st.nextToken());
		width = M;
		R = Integer.parseInt(st.nextToken());
		// �迭 �Է� >>�ִ��� ũ��
		origin = N>=M ? new char[N][N] : new char [M][M];
		moved = N>=M ? new char[N][N] : new char [M][M];
		for (int i = 0; i < height; i++) {
			inputLine = br.readLine();
			int k = 0;
			for (int j = 0; j < width * 2; j += 2) {
				origin[i][k++] = inputLine.charAt(j);
			}
		}
		// ���� ����
		String kinds = br.readLine();
		char kind;
		// ���� ����
			for (int c = 0; c < R*2; c += 2) {
				kind = kinds.charAt(c);
				switch (kind) {
				case '1': // ����
					upsideDown();
					break;
				case '2': // �¿�
					flipLeftRight();
					break;
				case '3':// ������ 09
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
				// origin�� moved ����
				copyToOrigin();
				printResult();
				System.out.println();
			}
		// ���� ���
		printResult();
	}
}
