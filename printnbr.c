#include <unistd.h>
#include "count.h"

void	printnbr(int n)
{
	char	c;

	if (n >= 10)
	{
		printnbr(n / 10);
	}
	c = (n % 10) + '0';
	write(1, &c, 1);
	return ;
}
