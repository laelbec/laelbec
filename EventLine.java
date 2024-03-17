/*
 * EventLine
 * 
 * A class to simulate a lineup of people waiting to enter
 * a sports/music event. Some people come alone and go to 
 * the back of the line, others bribe their way to a certain 
 * position. Sometimes someone buys a bunch of tickets at 
 * once so multiple people can be removed from the line and 
 * enter the event at the same time.
 */
public class EventLine {
	Queue<Person> lineup;
	//Do not add any other fields

	public EventLine() {
		//Do not change the constructor in any way
		lineup = new GenericQueue<Person>();
	}
	
	/*
	 * Purpose: add a person to the line to enter the event
	 * Parameter: Person p - the person to add
	 * Returns void - nothing
	 */
	public void enterLine(Person p) {
		// TODO: implement this
		lineup.enqueue(p);
	}
	
	/*
	 * Purpose: gets the number of people in line
	 * Parameters: none
	 * Returns: int - number of people in line
	 */
	public int peopleInLine() {
		// TODO: implement this
		return lineup.size(); // so it compiles
	}
	
	/*
	 * Purpose: handle the first person in line
	            (allow them to purchase their ticket
				 and enter into the event venue)
	 * Parameter: none
	 * Returns: Person - the person who gets their ticket
	 *                   and is no longer waiting in line
	 */
	public Person handleOne() {
		// TODO: implement this
		try{
			return lineup.dequeue();
		}
		catch(QueueEmptyException e) {
			return null;
		}
		 // so it compiles
	}
	
	/*
	 * Purpose: handle a whole group of people waiting in line
	 *          (allow a group to buy a number of tickets 
	 *           and all enter the event venue)
	 * Parameters: int num - the number of people
	 * Returns int - the number of people who were successfully
	 *               able to be removed from the line
	 */
	public int handleMultiple(int num) {
		// TODO: implement this
		int val = 0;
		for(int i = 0; i< num; i++){
			try{
				lineup.dequeue();
				val ++;
			}
			catch (QueueEmptyException e) {
				i = num;
			}
		}
		return val;
		// return -1; // so it compiles
	}
	
	/*
	 * Purpose: accept a bribe to put someone into a specific
	 *          position in the line to get into the event
	 * Parameters: Person p - the person entering the line
	 *             int pos - the position they are trying to get to
	 * Returns boolean - true if person added to line, false otherwise
	 */
	public boolean premiumEntry(Person p, int pos) {
		// TODO: implement this
		Queue<Person> newLine = new GenericQueue<Person>();
		int i = lineup.size();
		if(pos == i){
			lineup.enqueue(p);
			return true;
		}
		else if(pos< 0 || pos > i){
			return false;
		}
		while (i > pos+1){
			try{
			Person pp = lineup.dequeue();
			newLine.enqueue(pp);
			i--;
				}
			catch (QueueEmptyException e){
				return false;
			}
		}
		newLine.enqueue(p);
		i = pos +1;
		while(i>0){
			try{
			Person pp = lineup.dequeue();
			newLine.enqueue(pp);
			i--;
			}
			catch (QueueEmptyException e){
				return false;
			}
		
		}

		while(!newLine.isEmpty()){
			try{
				lineup.enqueue(newLine.dequeue());
			}
			catch (QueueEmptyException e){
				return false;
			}
		}
		return true;
    }
	
	
}
	
	