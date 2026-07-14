#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	i;
	int	*heap;

	heap = malloc (sizeof(int) * 10);
	if (heap == NULL)
	{
		exit (0);
	}
	i = 0;
	while (i < 10)
	{
		heap[i] = i;
		i++;
	}
	printf("%d\n", heap[5]);
	free(heap);
	return (0);
}
