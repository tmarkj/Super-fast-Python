#include <stdio.h>
#include <stdint.h>
#include <omp.h>


int sum(int64_t* array, int size) {
	
	int i;
	int sum = 0;

	#pragma omp parallel for
	for (i = 0; i < size; ++i) {
		sum += array[i];
	}

	return sum;
}


int main() {
	return 0;
}
