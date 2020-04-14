import java.util.ArrayList;
import java.util.Scanner;
import DynamicArray;

public class hm2{ //test kısmı
    public static void main(String[] args){
        Scanner getter = new Scanner(System.in);
        DynamicArray dynamicArray = new DynamicArray();
        for(int i = 0; i < 10; i++){
            Object x = getter.nextLine();
            dynamicArray.append(x);
            System.out.println("\n");
        }
        System.out.println(dynamicArray.remove());
        dynamicArray.append(123);
        dynamicArray.append("tempObject");
        System.out.println(dynamicArray.remove());
        getter.close();
    }
}
