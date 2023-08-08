import java.io.File; // Allow for the use of the file class by importing it
import java.io.FileNotFoundException; // Allow for the handling of errors
import java.io.BufferedReader;// Allow for sections of text files to be read at a time
import java.util.Scanner;// Allow for text files to be read by importing the scanner class
import java.util.ArrayList;// Allows for array lists to be used for storing data
import java.util.Arrays;//Allows for arrays to be used


public class Extract
{
    static int swaps;
    static int compares;
    public static void main(String[] args) throws FileNotFoundException{
        //Read the files and link them to a scanner name to be refered to later
        Scanner input = new Scanner(new File("Input219.txt"));
        Scanner comp =  new Scanner(new File("google-10000-english-no-swears.txt"));
        //Set up array lists that will be used to store the output from the scanners
        ArrayList<String> inputl= new ArrayList<String>();
        ArrayList<String> compl = new ArrayList<String>();
        //While there are available lines to read convert the input to a string and then make the strings lowercase 
        //to simplify comparisons later
            while (input.hasNextLine()) {
                String inputs = input.nextLine();
                inputs.toLowerCase();
                //Start a new scanner that scans the inputs already gathered and splits them in to words and gets 
                //rid of punctuation
                Scanner splitter = new Scanner(inputs);
                splitter.useDelimiter("\\W+");
                while (splitter.hasNext()){
                    String words = splitter.next();
                    //then add the split words to the relevant list
                    inputl.add(words);
                }
                //used to test the output of the list
                //System.out.println(inputl);
            }
            //Follows the same structure as the previous code but is related to the second file being the words that 
            //need to be compared against the input
            while (comp.hasNextLine()){
                String comps = comp.nextLine();
                comps.toLowerCase();
                Scanner splitterc = new Scanner(comps);
                splitterc.useDelimiter("\\W+");
                while (splitterc.hasNext()){
                    String wordsc = splitterc.next();
                    compl.add(wordsc);
                }
                //used to test the output of the list
                //System.out.println(compl);
            }
            //compare the words from the "google-10000-english-no-swears.txt" file against the input and keep
            //all of the words that are present in both files
            compl.retainAll(inputl);
            //used to test the final output
            //System.out.println(compl);
            //Close the scanners
            input.close();
            comp.close();
            //converts the compl ArrayList to an Array to be used in the merge sort
            String[] complists = compl.toArray(new String[0]);
            compl.toArray(complists);
            //Displays the unsorted list of all the words that are in both the input document and the comparrison document
            System.out.println("Unsorted list of words that appear in both documents: " + Arrays.toString(complists));
            //These empty strings are used to improve the readability of the output by creating new lines inbetween the different sections
            System.out.println("");
            //calls the mergeSort below to sort the array of complists
            mergeSort(complists, 0, complists.length - 1);
            //Displays the sorted list of words
            System.out.println("Sorted list of words that appear in both documents: " + Arrays.toString(complists));
            System.out.println("");
            //used to display the number of swaps and compares of the program (the output for both is 367)
            System.out.println("It took " + swaps + " swaps and " + compares +" comparisons to sort the array");
            
        }
        public static void mergeSort(String[] input, int from, int to) {
            if (from == to) {
                return;
            }
            //set the mid point of the array
            int mid = (from + to) /2;
            //sort the first half
            mergeSort(input, from, mid);
            //sort the second half
            mergeSort(input, mid + 1, to);
            //call the merge function below to merge the sorted and seperated arrays together
            merge(input, from, mid, to);
        }
        public static void merge(String[] input, int from, int mid, int to) {
            //finds the size of the array that needs merging
            int size = to - from + 1;
            //creates a new array of temp to hold the two halfs
            String[] temp = new String[size];
            //the elements that will be going in the first array
            int first = from;
            //the elements that will go in the second array
            int second = mid + 1;
            //shows what position of temp is currently available
            int pos = 0;
            //used to count the swaps and comparisons of the words from the input
            compares = 0;
            swaps = 0;
            //looks to compare first and second, if they are not past the end of their sections,
            //(first being past the size of the middle of the array, or second being past the end of the original array), 
            //put the smaller one into temp, also increase the compare on every loop and swaps when one of the words swaps places
            while (first <= mid && second <= to ){
                compares++;
                if (input[first].compareTo(input[second]) < 0){
                    temp[pos] = input[first];
                    first++;
                    swaps++;
                }else{
                    temp[pos] = input[second];
                    second++;
                    swaps++;
                }
                pos++;
            }

            //makes a copy of any remaining values from first
            while (first <= mid) {
                temp[pos] = input[first];
                first++;
                pos++;
            }
            //makes a copy of any remaining values from second
            while (second <= to){
                temp[pos] = input[second];
                second++;
                pos++;
            }

            //brings everything back from the temp array
            for (pos = 0; pos < size; pos++){
                input[from + pos] = temp[pos];
            }
        }
    }
