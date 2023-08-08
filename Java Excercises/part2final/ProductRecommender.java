public class ProductRecommender {
  ChoiceStrategy myStrategy;

  public static void main(String args[]) {
    ProductRecommender recommender=new ProductRecommender();
    recommender.doExample();
  }

  public void doExample() {
    Product p1=new Product("DeLorean DMC-12", 5, 1);
    Product p2=new Product("LDV Maxus", 1, 5);

   	 System.out.println("Current strategy: choose most futuristic");
  	 // Add code here to create a MostFuturisticStrategy and
   	 // print out the chosen vehicle according to this strategy

     //change the currently selected Strategy to Futuristic
     myStrategy =  new MostFuturisticStrategy();
     
     //set the result1 to be the outcome of the choose between function held in MostFuturisticStrategy
     Product result1 = myStrategy.chooseBetween(p1,p2);

     //used to test the output of the above function
     //System.out.println(result1.name);
     //an if statement to see if the result given by the choose between is equal to the first input, if it is 
     //print the first products name, else print the second products name
     if (result1.name == p1.name){
       System.out.println("Vehicle: " + p1.name);
     }
     else{
       System.out.println("Vehicle: " + p2.name);
     }

     System.out.println("Strategy changed: choose most practical");
     // Add code here to create a MostPracticalStrategy and
	   // print out the chosen vehicle according to this strategy
     
     //change the currently selected Strategy to Practical
      myStrategy =  new MostPracticalStrategy();

      //set the result2 to be the outcome of the choose between function held in MostPracticalStrategy
      Product result2 = myStrategy.chooseBetween(p1,p2);

      //used to test the output of result2
      //System.out.println(result2.name);
     //an if statement to see if the result given by the choose between is equal to the first input, if it is 
     //print the first products name, else print the second products name
     if (result2.name == p1.name){
       System.out.println("Vehicle: " + p1.name);
     }
     else{
       System.out.println("Vehicle: " + p2.name);
     }
	
    

  }
}

