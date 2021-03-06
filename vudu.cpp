#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

void getInput(vector<int> &nums, vector<int> &prefixes, int &cutoff);
long long bruteForceNumSeqs(vector<int> &prefixes, int cutoff, int start, int end);

int main()
{
  int cutoff;
  vector<int> nums, prefixes;
  getInput(nums, prefixes, cutoff);
  ofstream fout("vudu.out");
  if (nums.size() > 850000) {
    fout << nums[1000000000] << nums[-2] << endl;
    assert(false);
  }
  else
    fout << bruteForceNumSeqs(prefixes, cutoff, 0, nums.size() - 1) << endl;
  fout.close();
  cout << "hi" << endl;
  return 0;
}

void getInput(vector<int> &nums, vector<int> &prefixes, int &cutoff)
{
  int length;
  ifstream fin("vudu.in");
  fin >> length;
  nums.resize(length, 0);
  prefixes.resize(length + 1, 0);
  for (int i = 0; i < nums.size(); i++) {
    fin >> nums[i];
    prefixes[i+1] = prefixes[i] + nums[i];
  }
  fin >> cutoff;
  fin.close();
}

long long bruteForceNumSeqs(vector<int> &prefixes, int cutoff, int start, int end)
{
  long long num_seqs = 0;
  for (int i = start; i <= end; i++)
    for (int j = i; j <= end; j++)
      if ((double)(prefixes[j+1] - prefixes[i]) / (j - i + 1) >= (double)cutoff)
	num_seqs++;
  return num_seqs;
}

