

function perfomOperation(secondInteger, secondDecimal, secondString){
	// declare a variable named 'firstInteger' and initiaed with a value of 4
	const firstInteger = 4; 

	// declare a variable named 'firstDecimal' and initialize with floating-point value 4.0
	const firstDecimal = 4.0; 

	// declare a variable named 'firstString' and initialize with the string "HackerRank"
	const firstString = "HackerRank";

	// Write a code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to Number type)
	// on a new line 
	
	var sum = (firstInteger + secondDecimal);
	var sum1 = parseInt(sum, 10);
	console.log(sum1);

}


function main(){
	const secondInteger = readLine();
	const secondDecimal = readLine();
	const secondString = readLine();

	performOperation(secondInteger, secondDecimal, secondString);
} 
