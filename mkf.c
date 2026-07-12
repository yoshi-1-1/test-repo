#include <stdio.h>

int	main(void)
{
	int		i;
	int		j;
	FILE	*file;

	file = fopen("text.txt", "r");
	if (file == NULL)
	{
		printf("error\n");
		return (1);
	}
	if (fscanf(file, "%d,%d", &i, &j) != 2)
	{
		printf("error\n");
		fclose(file);
		return (1);
	}
	printf ("%d:%d", i, j);
	fclose (file);
	return (0);
}
