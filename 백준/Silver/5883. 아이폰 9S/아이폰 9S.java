import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        int max = 1;
        for (int i = 0; i < N; i++) {
            List<Integer> copy = new ArrayList<>(list);

            copy.removeAll(Arrays.asList(copy.get(i)));
            int count = 1;
            int prev = copy.get(0);
            for (int j = 1; j < copy.size(); j++) {
                    if (prev == copy.get(j)) {
                    count++;
                    max = Math.max(max, count);
                } else {
                    prev = copy.get(j);
                    count = 1;
                }
            }
        }

        System.out.println(max);

    }
}