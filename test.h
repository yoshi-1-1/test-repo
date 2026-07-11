struct	s_student
{
	int		year;
	int		clas;
	int		number;
	char	name[64];
	double	stature;
	double	weight;
};

typedef struct s_student	t_student;

void	student_print(t_student *data);
