#include <stdio.h>
#include <string.h>
#include "test.h"

int	main(void)
{
	t_student	data;

	data.year = 3;
	data.clas = 4;
	data.number = 18;
	strcpy(data.name, "MARIO");
	data.stature = 168.2;
	data.weight = 72.4;
	student_print(&data);
	return (0);
}

void	student_print(t_student *data)
{
	printf("%d\n", data->year);
	printf("%d\n", data->clas);
	printf("%d\n", data->number);
	printf("%s\n", data->name);
	printf("%f\n", data->stature);
	printf("%f\n", data->weight);
	return;
}
