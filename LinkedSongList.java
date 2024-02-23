public class LinkedSongList {
	// DO NOT ADD ANY MORE FIELDS OR METHODS
	private SongNode head;
	
	public LinkedSongList() {
		head = null;
	}

	public void addFront (Song s) {
		SongNode n = new SongNode(s);
		n.next = head;
		head = n;
	}

	public void addBack (Song s){
		SongNode n = new SongNode(s);
		if (head == null) {
			head = n;
		} else {
			addBackRec(head, n);
		}
	}
	
	private void addBackRec(SongNode cur, SongNode n) {
		if (cur.next == null) {
			cur.next = n;
		} else {
			addBackRec(cur.next, n);
		}
	}

	public boolean isEmpty() {
		return head == null;
	}

	public Song get (int position) {
		return getRec(head, 0, position);
	}
	
	private Song getRec(SongNode cur, int i, int position) {
		if (i == position) {
			return cur.getData();
		} else {
			return getRec(cur.next, i+1, position);
		}
	}

	/* Purpose: create a string representation of list
	 * Parameters: nothing	 
	 * Returns: String - the string representation of the list
	 */
	public String toString() {
		if (head == null) {
			return "{}";
		} else {
			return "{" + toStringRec(head) + "}";
		}
	}
	
	private String toStringRec(SongNode cur) {
		if (cur == null) {
			return "";
		} else if (cur.next == null) {
			return cur.getData().toString();
		} else {
			return cur.getData().toString() + ", " + toStringRec(cur.next);
		}
	}

	/*
	 * Purpose: Insert all elements from array into this linked list
	 * Parameters: Song[] array - the elements to add to this list
	 * Returns void - nothing
	 */
	public void buildFromArray(Song[] array) {
		buildFromArrayRec(array, array.length-1);
	}
	
	private void buildFromArrayRec(Song[] array, int i) {
		if (i < 0) {
			return;
		} else {
			addFront(array[i]);
			buildFromArrayRec(array, i-1);
		}
	}
	

	/*
	 * Purpose: gets the total number of songs in this list
	 * Parameters: none
	 * Returns: int - the number of songs in this list
	 */
	public int countSongs() {
		// TODO: Call a recursive helper method 
		if (head == null){
			return 0;
		}
		else{
			return countSongsRec(head); // so it compiles
		}
	}

	private int countSongsRec(SongNode cur){
		if(cur == null){
			return 0;
		}
		return 1 + countSongsRec(cur.next);
	}
	
		
	/*
	 * Purpose: gets the total duration of all songs in this list
	 * Parameters: none
	 * Returns: int - the total duration of all songs in this list
	 */
	public int totalDuration() {
		// TODO: Call a recursive helper method
		if(head == null){
			return 0;
		} else{
			return totalDurationRec(head);
		}
	}

	private int totalDurationRec(SongNode cur) {
		if(cur == null) {
			return 0;
		}
		return cur.getData().getDuration() + totalDurationRec(cur.next);
	}
	
	
	/*
	 * Purpose: counts the songs in this list by an artist with artistName
	 * Parameters: String artistName - the name of the artist to search for
	 * Returns: int - number of songs by artistName
	 */
	public int countSongsByArtist(String artistName) {
		// TODO: Call a recursive helper method
		if(head == null) {
			return 0;
		}
		else{
			return countSongsByArtistRec(head, artistName);
		}
	}

	private int countSongsByArtistRec(SongNode cur, String artistName) {
		if (cur == null){
			return 0;
		}
		else if(cur.getData().getArtist().equals(artistName)){
			return 1 + countSongsByArtistRec(cur.next, artistName);
		}
		else{
			return countSongsByArtistRec(cur.next, artistName);
		}

	}
	
	
	/*
	 * Purpose: determines whether this list contains a song by artistName
	 * Parameters: String artistName - the name of the artist to search for
	 * Returns: boolean - true if a song by artistName is found
	 */
	public boolean containsArtist(String artistName) {
		// TODO: Call a recursive helper method
		if(head == null){
			return false;
		}
		else{
			return containsArtistRec(head, artistName);
		}
	}

	private boolean containsArtistRec(SongNode cur, String artistName) {
		if(cur == null){
			return false;
		}
		else if(cur.getData().getArtist().equals(artistName)){
			return true;
		}
		else{
			return containsArtistRec(cur.next, artistName);
		}
	}
	
	
	/*
	 * Purpose: gets the longest song in the list
	 * Parameters: none
	 * Returns Song - the longest song in the list
	 *                or null if the list is empty
	 */
	public Song longestSong() {
		if(head == null) {
			return null;
		}
		else if(head.next == null) {
			return head.getData();
		}
		else{
			return longestSongRec(head, head.next);
		}
	}
	
	private Song longestSongRec(SongNode cur, SongNode other) {
		if(other == null){
			return cur.getData();
		}
		else if(cur.getData().getDuration() >= other.getData().getDuration()){
			return longestSongRec(cur, other.next);
		}
		else{
			return longestSongRec(other, other.next);
		}
	}
		
	/*
	 * Purpose: get the total duration of all songs in the list
	 *          before the first song by artistName
	 * Parameters: String artistName - the artist name to search for
	 * Returns int - the duration of all songs before the first
	 *               song by artistName, or -1 if no song by 
	 *               artistName is found.
	 */
	public int totalTimeUntilArtist(String artistName) {
		// TODO: Call a recursive helper method
		if(head == null){
			return -1;
		}
		else{
			return totalTimeUntilArtistRec(head, artistName, 0);
			}
	}

	private int totalTimeUntilArtistRec(SongNode cur, String artistName, int totalDur) {
		if (cur == null){
			return -1;
		}
		else if(cur.getData().getArtist().equals(artistName)){
			return totalDur;
		}
		else{
			return totalTimeUntilArtistRec(cur.next, artistName, totalDur+cur.getData().getDuration());
		}
	}
	
}