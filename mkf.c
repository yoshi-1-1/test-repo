#include <stdio.h>

int	main(void)
{
	FILE	*file;

	file = fopen ("text.txt", "w");
	fclose (file);
	return (0);
}
