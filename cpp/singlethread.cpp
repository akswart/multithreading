#include <iostream>
#include <cmath>
#include <iomanip> 
#include <chrono>
#include <vector>
#include <numeric>

using namespace std;
/*
Sieve prime checker
 */
int isPrime(long int x)
{
  if (x == 2) {
    return 1;
  }

  if (x%2 == 0) {
    return 0;
  }
  
  for (long int i = 3;i <= sqrt(x); i+=2)
    {
      if (x%i == 0) return 0;
    }
  
  return 1;
}

long int non_parallel_primes(float end_power) {
  // Make vector of increasing ints up to end_power
  vector<long int> vect((int)floor(pow(10,end_power)));
  long int nump = 0;
  iota(std::begin(vect), std::end(vect),1);

  for (long int i: vect) {
    if (isPrime(i)) {
      nump += 1;
    }
  }
  return nump;
}

float benchmark1(float end_power, int num_iter) {
  long int n;
  float t_sum = 0;

  for (int i = 0; i < num_iter; i++) {
    auto start = chrono::high_resolution_clock::now();
    
    n = non_parallel_primes(end_power);
 
    auto end = chrono::high_resolution_clock::now();
    auto time_taken = chrono::duration_cast<chrono::microseconds>(end - start);

    t_sum += time_taken.count()*pow(10.0,-6);
  }
  return t_sum/num_iter;
 
}

int main() {

  int num_iter = 50;
  float t_avg;
  for (float p = 5; p <= 8; p += .25) {
    t_avg = benchmark1(p,num_iter);
    printf("p =  %1.2f \tTime: %.3e \n",p,t_avg);
  }
  return 0;
}
