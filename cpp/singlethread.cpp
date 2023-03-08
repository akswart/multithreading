#include <iostream>
#include <cmath>
#include <iomanip> 
#include <chrono>
#include <vector>
#include <numeric>
#include <fstream>

using namespace std;
/*
Sieve prime checker
 */
int isPrime(long int x)
{
  if (x == 2 || x == 3) {
    return 1;
  }
  
  if (x%2 == 0 || x%3 == 0) {
    return 0;
  }
  
  for (long int i = 5;i <= sqrt(x); i+=6)
    {
      if (x%i == 0) return 0;
      if (x%(i+2) == 0) return 0;
    }



  return 1;
}

int isPrime2(long int x)
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

// Runs a series of benchmarks starting at start_power, ending at end_power
vector<vector<string>> benchmark_series(float start_power, float end_power, float step_power,
				int num_iter) {
  
  vector<vector<string>> result_vec;
  float t_avg;
  for (float p = start_power; p <= end_power; p += step_power) {
    t_avg = benchmark1(p,num_iter);
    vector<string> run_vec{"C++",to_string(p),to_string(num_iter),to_string(t_avg)};
    result_vec.push_back(run_vec);
    printf("Done with p: %.2f\t Time: %.4e\n",p,t_avg);
  }

  for (vector<string> i: result_vec) {
    for (string j: i) {
      printf("%s\t",j.c_str());
    }
    printf("\n");
  }

  return result_vec;
}

// Writes a vector of results to a csv file
int write_result_vector(vector<vector<string>> result_vect,string filename) {

  ofstream file;
  file.open(filename);
  // Setup column names
  file << "Language,End Power,Num Iter,Average,\n";
  for (vector<string> i: result_vect) {
    for (string j: i) {
      file << j << ",";
    }
    file << "\n";
  }
  file.close();
  return 1;
}

int main() {

  int num_iter = 1;
  float t_avg;
  vector<vector<string>> outvec = benchmark_series(1,9,.1,5);
  int status = write_result_vector(outvec,"../data/cpp_single.csv");
  return 0;
}

