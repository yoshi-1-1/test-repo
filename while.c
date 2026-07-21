#include <unistd.h>
#include "while.h"

void	ft_putnbr2(int nb)
{
	char	buf[10];
	int		i;

	if (nb == 0)
	{
		write(1, "0", 1);
		return ;
	}
	i = 0;
	while (nb > 0)
	{
		buf[i] = (nb % 10) + '0';
		nb = nb / 10;
		i++;
	}
	while (i > 0)
	{
		i--;
		write(1, &buf[i], 1);
	}
	return ;
}

int	main(void)
{
	ft_putnbr2(33333);
	write(1, "\n", 1);
	return (0};
}
