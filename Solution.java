
import java.lang.*;
import java.util.*;
 
class TestClass {
    
    public static void inverse(String str){
        char[] arr = str.toCharArray();
        
        for(int i = 0; i<arr.length;i++){
            char ch = arr[i];
            if(Character.isLowerCase(ch))
                arr[i] = Character.toUpperCase(ch);
            else if(Character.isUpperCase(ch))
                arr[i] = Character.toLowerCase(ch);
        }
        String solution = "";
        for(int i=0;i<arr.length;i++){
            solution +=arr[i];
        }
        System.out.print( solution+" ");
    }
    
    public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running
         * Use either of these methods for input
 
        //BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
 
        //Scanner
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
 
        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */
 
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");
        for(int i = 0; i<arr.length;i++)inverse(arr[i]);
            
        //System.out.println(arr[1]);
    }
}