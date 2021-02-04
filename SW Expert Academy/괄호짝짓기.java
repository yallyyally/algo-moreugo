import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.HashMap;
import java.util.Stack;
 
public class Solution {
    static ArrayList<Character> stack = new ArrayList<>();
    static boolean flag;
    static boolean emptyFlag;
    static HashMap<Character, Character> map = new HashMap<>(); // 닫는괄호-여는괄호.
 
    public static char pop() {
        int len = stack.size();
 
        if (len == 0) {
            return 'x';
        } else {
            return stack.remove(len - 1);
        }
    }
    public static void push(char input) {
        stack.add(input);
    }
    public static boolean empty() {
        if(stack.size() == 0)
            return true;
        else
            return false;
    }
     
    public static void updateStack(char input) {
        char outChar;
 
        outChar = pop();
         
        if(outChar == 'x')
            flag = false;
         
        else if (map.get(input) != outChar)
            flag = false;
    }
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int length;
        String inputLine;
        char inputChar;
        int res = 1;
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        map.put('>', '<');
        for (int t = 0; t < 10; t++) {
            stack.clear();
            flag = true; // 디폴트는 트루.
            length = Integer.parseInt(br.readLine());
            inputLine = br.readLine();
            for (int i = 0; i < length; i++) {
                inputChar = inputLine.charAt(i);
                // 여는 괄호면 push, 닫는 괄호면 pop
                if (map.get(inputChar) == null)
                    push(inputChar);
                else
                    updateStack(inputChar);
                if (!flag) {
                    res = 0;
                    break;
                }
            }
            if (flag) {
                if (empty())
                    res = 1;
                else
                    res = 0;
            }
            System.out.println("#" + (t + 1) + " " + res);
        }
    }
}