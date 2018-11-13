
public class Problem3 {
	private long starTime;
	private long endTime;
	private long elapsedTime;
	
	public void aLoop(int N){
		this.starTime = System.currentTimeMillis();
		int sum = 0;
		for (int i = 0; i < 23; i ++){
			for (int j = 0; j < N ; j ++){
				sum = sum + 1;
			}
		}	
		this.endTime = System.currentTimeMillis();
		this.elapsedTime = this.endTime - this.starTime;
	}

	public void bLoop(int N){
		this.starTime = System.currentTimeMillis();
		int sum = 0;
		for ( int i = 0; i < N; i ++){
			for (int k = i; k < N; k ++){
				sum = sum + 1;
			}
		}
		this.endTime = System.currentTimeMillis();
		this.elapsedTime = this.endTime - this.starTime;
	}
	
	public int foo(int n, int k){
		if (n <= k){
			
			return 1;
		} else {
			return foo(n/k, k) + 1;
		}
	}


/*
	public int fooHelp(int n, int k){
		try {
			Thread.sleep(100);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.starTime = System.currentTimeMillis();
		int result = foo(n, k);
		this.endTime = System.currentTimeMillis();
		this.elapsedTime = this.endTime - this.starTime;
		return result;
	}
*/
	public int fooHelp(int n, int k){
		/*
		try {
			Thread.sleep(100);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		*/
		this.starTime = System.nanoTime();
		int result = foo(n, k);
		this.endTime = System.nanoTime();
		this.elapsedTime = this.endTime - this.starTime;
		return result;
	}


	
	public long getETime(){
		return this.elapsedTime;
	}
	public long getStarTime(){
		return this.starTime;
	}
	public long getEndTime(){
		return this.endTime;
	}

	// Main Function
	public static void main(String [] args){
		Problem3 testA = new Problem3();
		Problem3 testB = new Problem3();
		Problem3 testC = new Problem3();
		
		int aBase = 10000;
		int bBase = 1000;
		int cBase = 100;

		System.out.println(" For the first loop: ");
		for (int i = 1; i <= 10; i++){
			testA.aLoop(aBase * i);
			System.out.println("when N = " + i*aBase + ", it costs " + testA.getETime() + " time");
		}
		System.out.println("-----------------------------------------------------------------------");

		System.out.println(" For the second loop: "); 
		for (int i = 1; i <= 10; i++){
			testB.bLoop(bBase * i);
			System.out.println("When N = " + i*bBase + ", it costs " + testB.getETime() + " time");
		}
		System.out.println("-----------------------------------------------------------------------");

		System.out.println(" For the Recursion: ");
		for (int i = 10; i <= 100000; i*=10){
			testC.fooHelp(cBase * i, 2);
			System.out.println("When N = " + i*cBase + ", it costs " + testC.getETime() + " time");
		}
		System.out.println("-----------------------------------------------------------------------");
	}
}	

