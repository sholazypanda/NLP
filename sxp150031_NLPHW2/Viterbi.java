import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Viterbi {
	
	
	
	private  List<Double> intialProbList;
	private List<String> stateList;
	private int N = 2;
	private String inputObsSequence;
	HashMap<String,Double> conditionalProbMap;
	HashMap<String,Double> transitionProbMap;
	private double viterbiMatrix[][];
	private String backPointer[][];
	private char strObservations[];
	public Viterbi(String obsSequence){
		inputObsSequence = obsSequence;
		conditionalProbMap = new HashMap<String,Double>();
		transitionProbMap = new HashMap<String,Double>();
		
		conditionalProbMap.put("1|HOT",0.2);
		conditionalProbMap.put("2|HOT",0.4);
		conditionalProbMap.put("3|HOT",0.4);
		conditionalProbMap.put("1|COLD",0.5);
		conditionalProbMap.put("2|COLD",0.4);
		conditionalProbMap.put("3|COLD",0.1);
		
		transitionProbMap.put("HOT|HOT",0.7);
		transitionProbMap.put("COLD|COLD",0.6);
		transitionProbMap.put("HOT|COLD",0.3);
		transitionProbMap.put("COLD|HOT",0.4);
		
		intialProbList = new ArrayList<Double>();
		intialProbList.add(0,0.8);
		intialProbList.add(1,0.2);
		stateList = new ArrayList<String>();
		stateList.add(0,"HOT");
		stateList.add(1,"COLD");
		viterbiMatrix = new double[N][inputObsSequence.length()]; // not considering final states
		backPointer = new String[N][inputObsSequence.length()];
	    strObservations= inputObsSequence.toCharArray();
	}
	
	
	public String[] findViterbi(){
		
		
		// initialization step
		for(int i=0;i<N;i++){ // for each state 1 to N
			String key = strObservations[0]+"|"+stateList.get(i);
			//System.out.println(key);
			double obsGivenState = conditionalProbMap.get(key);
			//System.out.println(obsGivenState);
			
			viterbiMatrix[i][0] =  intialProbList.get(i) * obsGivenState;
			//System.out.println("hhh"+viterbiMatrix[i][0]);
			backPointer[i][0] = stateList.get(i);
		}
		
		for(int t=1;t<strObservations.length;t++){
			String[][] backTrack = new String[N][inputObsSequence.length()];
			for(int s=0;s<N;s++){
				double res = -1;
				int state;
				for(int prevStates = 0;prevStates<N;prevStates++){
					double transProb = transitionProbMap.get(stateList.get(prevStates)+"|"+stateList.get(s)) ;
					double emissionProb = conditionalProbMap.get(strObservations[t]+"|"+stateList.get(s));
					double resProb = viterbiMatrix[prevStates][t-1] * transProb * emissionProb;
					//System.out.println(resProb);
					if(resProb > res){
						res = resProb;
						state = prevStates;
						viterbiMatrix[s][t] = resProb;
						
						//System.out.println("state from"+stateList.get(s));
						System.arraycopy(backPointer[state], 0, backTrack[s], 0, t);
						backTrack[s][t] = stateList.get(s);
					
					}
				}
			}
			backPointer = backTrack;
			
		}
		
		double newProb = -1;
        int state = 0;
        for (int s=0;s<N;s++)
        {
            if (viterbiMatrix[s][inputObsSequence.length()-1] > newProb)
            {
                newProb = viterbiMatrix[s][inputObsSequence.length()-1];
                state = s;
            }
        }

        return backPointer[state];
	}
	
	
	
	public static void main(String args[]){
		String inputObsSequence="";
		if(args.length<1){
			inputObsSequence="331122313";
		}
		else{
			inputObsSequence = args[0];
		}
		Viterbi vObj = new Viterbi(inputObsSequence);
		String arr[]= vObj.findViterbi();
		System.out.println(Arrays.toString(arr));
	}
}
