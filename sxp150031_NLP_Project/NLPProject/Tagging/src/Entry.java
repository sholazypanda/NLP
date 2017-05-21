
import java.util.List;

public class Entry {
	
	
	public static void main(String[] args) {
		String trainPOSTagged;
		String testPOSTagged;
		if(args.length < 1 ){
			trainPOSTagged = "src/train.txt";	
			testPOSTagged = "src/test.txt";
		} else {
			trainPOSTagged = args[0];
			testPOSTagged = args[1];
		}
		
		HMMTrain hmmObj = new HMMTrain();
		hmmObj.getWordsAndTags(trainPOSTagged);
		hmmObj.updateTransitionEmission();
		hmmObj.train();
		hmmObj.displayResults();
		
		ViterbiTest vobj = new ViterbiTest();
		vobj.getWordsAndTags(testPOSTagged);
		vobj.test(hmmObj.getEmissionProb(),hmmObj.getTransitionProb(),hmmObj.getWordTag());
	}
	
	
}
