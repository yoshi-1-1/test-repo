#include <unistd.h>
#include "count.h"

int	main(void)
{
	count(12345678902);
	write(1, "\n", 1);
	return (0);
}
