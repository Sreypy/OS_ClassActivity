package OSclass_activity;
import java.util.concurrent.*;
import java.util.stream.IntStream;

public class ThreadExample {
    public static void main(String[] args) {
        // SingleThreadExecutor
        ExecutorService singleThread = Executors.newSingleThreadExecutor();
        singleThread.submit(() -> System.out.println("SingleThreadExecutor task executed by " + Thread.currentThread().getName()));
        singleThread.shutdown();

        // CachedThreadPool
        ExecutorService cachedPool = Executors.newCachedThreadPool();
        for (int i = 0; i < 5; i++) {
            final int id = i;
            cachedPool.submit(() -> System.out.println("CachedThreadPool task " + id + " executed by " + Thread.currentThread().getName()));
        }
        cachedPool.shutdown();

        // ForkJoinPool (parallelism)
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        forkJoinPool.submit(() -> {
            IntStream.range(0, 10).parallel().forEach(i ->
                System.out.println("ForkJoin task " + i + " executed by " + Thread.currentThread().getName())
            );
        }).join();
        forkJoinPool.shutdown();
    }
}