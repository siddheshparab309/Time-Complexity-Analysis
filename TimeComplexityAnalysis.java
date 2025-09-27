public class TimeComplexityAnalysis {
    public static void main(String[] args) {

        long[] nValues = {1000, 5000, 10000, 50000, 100000, 500000, 1000000};

        System.out.printf("%12s %20s %26s%n", "n", "Experimental(ns)", "Theory (n*log*n*loglogn)");
        System.out.println("---------------------------------------------------------------");

        for (long n : nValues) {
            long startTime = System.nanoTime();
            simulateCodeSnippet(n);
            long endTime = System.nanoTime();
            long duration = endTime - startTime;
            double theory = n * Math.log(n) * (Math.log(Math.log(n)));
            System.out.printf("%12d %20d %26.6f%n", n, duration, theory);
        }
    }

    public static void simulateCodeSnippet(long n) {
        int j = 2;
        while (j < n) {
            int k = 2;
            while (k < n) {
                int next = (int) (k * Math.sqrt(k));
                if (next <= k) {
                    k += 1;
                } else {
                    k = next;
                }
            }
            j += Math.max(1, j / 2);
        }
    }
}
