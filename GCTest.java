import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.CountDownLatch;
import java.util.*;

public class GCTest{

    public static int MAX_ALLOC_SIZE = 10000;
    public static int NUM_ITS = 10000;
    public static int MAX_LIST = 100;
    public static int NTHREADS = 4;
    public static int SERVER_PORT = 9090;
    public static final String SERVER = "server";
    public static final String CLIENT = "client";

    public static void main(String... args) throws Exception{
        // parse args
        if(args.length != 4){
            System.err.println("I need 4 args (max alloc size, num its, max cache, nthreads), you gave me " + args.length);
            System.exit(0);
        }
        // collect the parameters
        MAX_ALLOC_SIZE = Integer.parseInt(args[0]);
        NUM_ITS = Integer.parseInt(args[1]);
        MAX_LIST = Integer.parseInt(args[2]);
        NTHREADS = Integer.parseInt(args[3]);
        CountDownLatch ltc = new CountDownLatch(NTHREADS);
        // and start the threads
        ArrayList<DummyThread> dthreads = new ArrayList<>();
        
        int iter = 100;
        for(int i = 0; i < iter; i++) {
            for(int j = 0; j < NTHREADS; ++j){
                dthreads.add(new DummyThread(ltc));
            }
            
            for(int j = 0; j < NTHREADS; j++) {
                dthreads.get(j).start();
                
            }
            
            for(int j = 0; j < NTHREADS; j++) {
                dthreads.get(j).join();
            }
            
            dthreads.clear();
            
            ltc.await();
        }
        
        
        System.out.println("done");

    }

    private static class DummyThread extends Thread{

        private CountDownLatch ltc = null;

        public DummyThread(CountDownLatch ltc){
                this.ltc = ltc;
        }

        @Override
        public void run(){
            DummyList lst = new DummyList(MAX_LIST);
            for(int i = 0; i < NUM_ITS; ++i){
                    Dummy d = new Dummy();
                    lst.add(d);
            }
            ltc.countDown();
            System.out.println("Thread " + Thread.currentThread().getName() + " is done");
        }
    }

    private static class Dummy{

        private char[] element = null;

        public Dummy(){
            element = new char[ThreadLocalRandom.current().nextInt(1, GCTest.MAX_ALLOC_SIZE)];
        } 

    }

    private static class DummyList{

        private int maxSize;
        private int current;
        private List<Dummy> elements = new ArrayList<Dummy>();

        public DummyList(int maxSize){
            this.maxSize = maxSize;
            current = 0;
        }

        public void add(Dummy d){
            if(current >= maxSize) elements.clear();
            elements.add(d);
        }
    }	

}
