public class MostFuturisticStrategy implements ChoiceStrategy {
 	 // Complete this with an implementation of
	// chooseBetween(Product a, Product b) which returns
	// Product a if its futuristicness is greater than or equal
	// to that of b; and returns Product b otherwise
	//uses an instance of chooseBetween and change it to the follwing code when called in the ProductReccomender
	//takes Product a and Product b as inputs
	//then checks the Products Functionality which is a variable initialized in the Product class and 
	//the value is taken from the input given in the ProductRecommender
	//if the Functionality of a is higher than or equal to the Functionality of b then a is returned else b is returned
	public Product chooseBetween(Product a,Product b){
		if (a.futuristicness >= b.futuristicness){
			return a;
		}
		else {
			return b;
		}
	}
}


