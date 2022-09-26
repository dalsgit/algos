import java.util.ArrayList;
import java.util.List;

import javax.swing.plaf.ColorUIResource;

public class Triangle {
    protected List<List<Integer>> triangle = new ArrayList<>();
    
    public void generate(int numRows) {
        System.out.println("Starting to generate triangle: " + numRows);
        if (numRows < 1) return;
        List<Integer> firstRow = new ArrayList<Integer>();
        firstRow.add(1);
        triangle.add(firstRow);
        for(int i=1; i<numRows; i++) {
            List<Integer> prev = triangle.get(i-1);
            List<Integer> current = new ArrayList<Integer>();
            current.add(1);
            triangle.add(current);
            for(int j=1; j<i; j++) {
                current.add(prev.get(j-1) + prev.get(j));
            }
            current.add(1);
        }
    }
    
    public static void main(String[] args) {
        Triangle t = new Triangle();
        t.generate(4);
        System.out.println(t.triangle);
    } 
}