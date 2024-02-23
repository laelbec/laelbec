public class A5Exercises {

	/*
	 * Purpose: change all occurrences of x to y in the given list
	 * Parameters: List<T> theList - the list to search through
	 *			   T x - the value to change
	 *			   T y = the value to change all x's to
	 * Returns: void - nothing
	 */
	public static<T> void changeXToY(List<T> theList, T x, T y) {
		// TODO: Call a recursive helper method
		changeXToYRec(theList, x, y, 0);
	}

	private static<T> void changeXToYRec(List<T> theList, T x, T y, int i) {
		if(i < theList.size()){
			if(theList.get(i) == x) {
				theList.change(i, y);
			}
			changeXToYRec(theList, x, y, i+1);
		}
	}
	
	/*
	 * Purpose: count the total number of odd values in this list
	 * Parameters: List<Integer> theList - the list of Integers
	 * Returns: int - the total number of odd values found
	 */
	public static int countOdd(List<Integer> theList) {
		// TODO: Call a recursive helper method
		if(theList.isEmpty()) {
			return 0;
		}
		else{
			return countOddRec(theList, 0);
		}
	}

	private static int countOddRec(List<Integer> theList, int x){
		if(x == theList.size()) {
			return 0;
		}
		else if(theList.get(x) % 2 == 0) {
			return 0 + countOddRec(theList, x+1);
		}
		else{
			return 1 + countOddRec(theList, x+1);
		}
	}
	

	/*
	 * Purpose: get the largest sequence of odd values found in a row
	 * Parameters: List<Integer> theList - the list of Integers
	 * Returns: int - the largest sequence of odd values found in a row
	 */
	public static int countMostOddInARow(List<Integer> theList) {
		// TODO: Call a recursive helper method
		if(theList.isEmpty()) {
			return 0;
		}
		else{
			return countMostOddInARowRec(theList, 0, 0, 0);
		}
	
	}

	private static int countMostOddInARowRec(List<Integer> theList, int i, int curCount, int maxCount) {
		if(theList.size() == 1){
			if(theList.get(i) %2 == 0){
				return 0;
			}
			else{
				return 1;
			}
		}
		else if (i == theList.size()){
			return maxCount;
		}
		else if(theList.get(i) %2 != 0) {
			return countMostOddInARowRec(theList, i+1, curCount +1, maxCount);
		}
		else{
			if(curCount > maxCount){
				maxCount = curCount;
				curCount = 0;
			}
			else{
				curCount = 0;
			}
			return countMostOddInARowRec(theList, i+1, curCount, maxCount);
		}
	}
	
	
	/*
	 * Purpose: count the elements found in between the first two x's
	 * Parameters: List<Integer> theList - the list of Integers
	 *             int x - the values to search for
	 * Returns: int - the number of values in the list found 
	 *                between the first 2 occurrences if x,
	 *                or -1 if there are not 2 x's in the list.
	 */
	public static int countBetweenX(List<Integer> theList, int x) {
		// TODO: Call a recursive helper method
		return countBetweenXRec(theList, x, 0, 0, 0);
	}

	private static int countBetweenXRec(List<Integer> theList, int x, int i, int count, int xCount){
		if(i == theList.size() && xCount != 2){
			return -1;
		}
		else if (xCount == 2) {
			return count;
		}
		else if(theList.get(i)==x){
			xCount++;
			return countBetweenXRec(theList, x, i+1, count, xCount);
		}
		else if(xCount == 1 && theList.get(i)!=x){
			count++;
			return countBetweenXRec(theList, x, i+1, count, xCount);
		}

		else{
			return countBetweenXRec(theList, x, i+1, count, xCount);
		}
	}
	
}