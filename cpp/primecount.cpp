#include <iostream>
#include <cmath>
#include <iomanip> 
#include <chrono>
using namespace std;
/*
Sieve prime checker
 */
int isPrime(long int x)
{
  for (long int i = 2;i <= sqrt(x); i++)
    {
      if (x%i == 0) return 0;
    }
  
  return 1;
}

int primeRange(long int lower, long int upper, bool print) {
  int primeCount = 0;
  for (long int i = lower; i <= upper; i++)
    {
      primeCount += isPrime(i);

    }
  if (print) {
  cout << "\nThere are " << primeCount << " primes between " << lower << " and " << upper << endl;
  }
  return primeCount;

}




/*
Determines the probabilty that a random number 
is a prime within an input range
 */
int main()
{
  long int lower;
  long int upper;
  int count = 0;
 tryAgain:
  cout << "Enter lower bound:\n";
  cin >> lower;
  cout << "Enter upper bound:\n";
  cin >> upper;

  if (upper < lower) {
    
    count++;
    if (count >= 3) {
      cout << "Dont be a moron\n";
      return 0;
    }
    else
      {	   
	cout << "Lower and upper are flipped, please try again\n";
	goto tryAgain;
      }
  }


  cout << "Lower: " << lower <<  " Upper: " << upper << "\n";
  // Now that we have our bounds, lets iterate through an array of integers from lower to upper
  // Checking if each are prime or not

  auto start = chrono::high_resolution_clock::now();
  primeRange(lower, upper, true);
  
  auto end = chrono::high_resolution_clock::now();
  auto time_taken = chrono::duration_cast<chrono::microseconds>(end - start);
  cout << "\n_____________\n" << time_taken.count()*pow(10.0,-6) << " seconds\n";
  return 0;
}
    
