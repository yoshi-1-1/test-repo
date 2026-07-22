#include <unistd.h>
#include "count.h"

void	count(long nb)
{
	long	i;

	if (nb == 0)
	{
		i = 1;
	}
	else
	{
		i = 0;
		while (nb != 0)
		{
			nb = nb / 10;
			i++;
		}
	}
	printnbr(i);
	return ;
}
