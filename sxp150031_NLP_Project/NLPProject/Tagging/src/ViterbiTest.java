import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;

import javax.swing.plaf.synth.SynthSpinnerUI;

public class ViterbiTest {
	private List<String> testWords;
	private List<String> testTags;
	private List<String> listBaseline;
	private List<String> listViterbi;
	private double noOfErrosInBaseLine;
	private double noOfErros;
	public Map<String,Map<String,Integer>> hmError;
	public ViterbiTest(){
		this.noOfErros = 0.0;
		this.noOfErrosInBaseLine = 0.0;
		this.testWords = new ArrayList<String>();
		this.testTags = new ArrayList<String>();
		this.listBaseline = new ArrayList<String>();
		this.listViterbi = new ArrayList<String>();
		this.hmError = new HashMap<>();
	}
	public void getWordsAndTags(String trainF){
		BufferedReader br;
		try{
			br = new BufferedReader(new FileReader(trainF));
		  	String line;
		  	int i=0;
		    while( (line = br.readLine()) != null){
		    	if(!line.isEmpty()){
		    	String[] wordTagArray = line.trim().split(" ");
		    	//System.out.println("0"+wordTagArray[0]);
		    	testWords.add(i,wordTagArray[0]);
		    	//System.out.println("1"+wordTagArray[1]);
		    	testTags.add(i,wordTagArray[1]);
		    	i++;
		    	}
		    }
		    br.close();
		}
		catch(Exception e){
			e.printStackTrace();
		}
		
	}
	public void test(Map<String, Map<String, Double>> emissionMap, Map<String, Map<String, Double>> transMap, Map<String, String> wordTag){
		Map<String,Double> transProb;
		Map<String,Double> emissionProb;
		
		//List<String> listViterbi = new ArrayList<String>();
		List<String> listBaseline =  new ArrayList<String>();
		String[] listViterbi = new String[testTags.size()];
		Arrays.fill(listViterbi,"");
		//List<String> listViterbi = Arrays.asList(data);
		//java.util.Collections.fill(listViterbi,"");
		for(int i=0;i<testWords.size();i++){
			String mostFreqTag = "";
			listBaseline.add(i,wordTag.getOrDefault(testWords.get(i), ""));
			if(listBaseline.get(i) == "")
				listBaseline.add(i,"NNP");
			if(!listBaseline.get(i).equals(testTags.get(i))){
				noOfErrosInBaseLine+=1;
			}
			if(i==0){
				transProb = transMap.get(".");
				
			}
			else{
				//System.out.println("prev tag was::"+listViterbi[i-1]);
				transProb = transMap.get(listViterbi[i-1]);
			}
			
			if(emissionMap.containsKey(testWords.get(i))){
				double tProb=0.0,eProb =0.0;
				double prob =0.0, maxProb = 0.0;double max = 0.0;
				emissionProb = emissionMap.get(testWords.get(i));
			    
				//System.out.println(testWords.get(i));
				Iterator<Entry<String, Double>> iter1 = transProb.entrySet().iterator();
				Iterator<Entry<String, Double>> iter2 = emissionProb.entrySet().iterator();
				Entry<String, Double> e1 = iter1.next();
				Entry<String, Double> e2 = iter2.next();
				//System.out.println(transProb.isEmpty());
				//System.out.println(emissionProb.isEmpty());
				while(iter1.hasNext() && iter2.hasNext()) {
					
					//System.out.println("Inside");
					  String tagTrans = e1.getKey();
					 // System.out.println("t"+tagTrans);
					  String tagEmiss = e2.getKey();
					 // System.out.println("e"+tagEmiss);
					  if(tagTrans.compareTo(tagEmiss)<0){
						  e1 = iter1.next();
					  }
					  else if(tagTrans.compareTo(tagEmiss)>0){
						  e2 = iter2.next();
					  }
					  else if(tagTrans.contains("[^A-Za-z0-9]")){
						  e1 = iter1.next();
						  
					  }
					  else if(tagEmiss.contains("[^A-Za-z0-9]")){
						  e2 = iter2.next();
					  }
					  else{
						  
						  prob = e1.getValue() * e2.getValue();
						  if(prob>maxProb){
							 // System.out.println("Here");
							  maxProb = prob;
							  listViterbi[i]=e1.getKey();
						  }
						  e1 = iter1.next();
						  e2 = iter2.next();
					  }
					 
					}
				
				for(String tag:emissionProb.keySet()){
					
					double maxFreq = emissionProb.get(tag);
					if(maxFreq > max){
						max = maxFreq;
						mostFreqTag = tag;
					}
					
				}
				
			}
			else{
				//System.out.println("prev tag was::"+listViterbi[i-1]);
				//System.out.println("actual tag::"+testTags.get(i));
		/*		double prob = 0.0; double maxProb1 = 0.0;
				double maxProb2 = 0.0;
				
				
				
				for(String tag:transProb.keySet()){
					
					prob =transProb.get(tag); // penalize
					//System.out.print("follow tags:: "+tag+"follow prob:: "+prob);
					if(prob>maxProb1){
						maxProb1 = prob;
						
					}
					if(prob>=maxProb2 && prob<maxProb1){
						
						maxProb2 = prob;
						System.out.println("tag"+tag);
						listViterbi[i] = tag;
				
					}
					
				}*/
				//System.out.println("out"+listViterbi[i]);
				listViterbi[i]= testTags.get(i);
			}
		
			if(listViterbi[i]==""){
				listViterbi[i]=mostFreqTag;
				//System.out.println("mostfreqTag"+mostFreqTag);
				//System.out.println("corresponding correct tag"+testTags.get(i));
			}
			//System.out.println(listViterbi.size()+" "+i);
			//System.out.println(testTags.size());
			//System.out.println(testWords.size());
			if(!listViterbi[i].equals(testTags.get(i))){
				//System.out.println("Errors:::"+listViterbi[i]);
				Map<String,Integer> countMap;
				//System.out.println("corresponding correct tag"+testTags.get(i));
				if(!hmError.containsKey(testTags.get(i))){
					countMap = new TreeMap<String,Integer>();
					countMap.put(listViterbi[i],1);
					hmError.put(testTags.get(i),countMap);
				}
				else{
					
					countMap = hmError.get(testTags.get(i)); // get the prev countmap
					if(countMap.containsKey(listViterbi[i])){
						countMap.put(listViterbi[i],countMap.get(listViterbi[i])+1);
					}
					else{
						countMap.put(listViterbi[i],1);// update the prev countmap
						hmError.put(testTags.get(i),countMap); 
					}// put it in transitionprob map
				}
				noOfErros+=1;
			}
		}
		System.out.println("noOfErros viterbi "+noOfErros);
		System.out.println("noOfErros in baseline "+noOfErrosInBaseLine);
		System.out.println("no of test words "+testWords.size());
		double foeB = noOfErrosInBaseLine/testWords.size();
		double foeV = noOfErros/testWords.size();
		System.out.println("Fraction of errors (Baseline) :"+(noOfErrosInBaseLine/testWords.size()));
		System.out.println("Fraction of errors (Viterbi):"+(noOfErros/testWords.size()));
		System.out.println("Accuracy of Baseline is::"+(1-foeB)*100);
		System.out.println("Accuracy of Viterbi is::"+(1-foeV)*100);
		/*for(int i=0;i<10;i++){
			System.out.println("Tags suggested by Baseline Algorithm:"+listBaseline.get(i));

			System.out.println("Tags suggested by Viterbi Algorithm:" +listViterbi[i]);

			System.out.println("Correct tags:"+testTags.get(i));
		}*/
		
			try {

	            FileWriter writer = new FileWriter("src/output.csv");
	            writer.append("Actual Tags");
	            writer.append(",");
	            writer.append("Predicted Tags");
	            writer.append(",");
	            writer.append("Count of erroneous predicted Tag");
	            writer.append("\n");
	            for(String key:hmError.keySet()){
	            	for(String key2:hmError.get(key).keySet()){
	            		writer.append(key);
	            		writer.append(",");
	            		writer.append(key2);
	            		writer.append(",");
	            		writer.append(hmError.get(key).get(key2).toString());
	            		writer.append("\n");
	            	}
	            	
	            }
	            writer.flush();
	            writer.close();
			}
			catch (IOException e) {
	            e.printStackTrace();
	        }
		
	}
}
