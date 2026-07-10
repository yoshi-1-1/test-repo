#include <stdio.h>
#include <string.h>
#include "test.h"

int	main(void)
{
	struct s_student	data;

	strcpy(data.name, "MARIO");
	printf("%s\n", data.name);
	return (0);
}
