import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter code: ");
		int code = input.nextInt();

		System.out.println("This is the code " + code);

		input.close();
	}
}