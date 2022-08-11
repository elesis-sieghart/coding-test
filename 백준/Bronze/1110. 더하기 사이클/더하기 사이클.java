import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String strNum = st.nextToken();
		br.close();
		int num = Integer.parseInt(strNum);
		int nextNum = 0;
		int c, f, cycle = 0;
		
		c = (num/10 + num%10) %10;
		nextNum = Integer.parseInt(String.valueOf(num%10)+String.valueOf(c));
		cycle++;
		while(num!=nextNum) {
			f = (nextNum/10 + nextNum%10) %10;
			nextNum = Integer.parseInt(String.valueOf(nextNum%10)+String.valueOf(f%10));
			cycle++;
		}
		System.out.println(cycle);
	}
}
