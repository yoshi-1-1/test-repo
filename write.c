#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

int	main(void)
{
	int	n;
	int	*ptr;

	n = 5;
	ptr = &n;
	*ptr = 8;
	ft_putchar(n + '0');
	ft_putchar('\n');
	return (0);
}
