#include <unistd.h>
#include "ft_putnbr.h"

void	ft_putnbr(int nb)
{
	char	c;

	if (nb >= 0 && nb <= 9)
	{
		c = nb + '0';
		write(1, &c, 1);
	}
	if (nb >= 10)
	{
		ft_putnbr(nb / 10);
		ft_putnbr(nb % 10);
	}
	return ;
}

int	main(void)
{
	ft_putnbr(119);
	write(1, "\n", 1);
	return (0);
}
