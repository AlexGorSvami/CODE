my_vector1 <- [1:50]
my_vector2 <- [1,2,3]

my_vector2[c(1,2,3)]
my_vector2[1:3]

my_vector1 + 10

my_vector2 == 0
my_vector1 > 30

x <- 23

my_vector1 > 23
my_vector1 > x
x == 23

my_vector2 > 0
my_vector2[my_vector2 > 0]
my_vector2[my_vector2 < 0]
my_vector2[my_vector2 == 0]

my_vector1[my_vector1 > 20 & my_vector1 < 30]
my_numbers <- my_vector1[my_vector1 > 20 & my_vector1 < 30]

v1 <- c(165, 178, 180, 181, 167, 178, 187, 167, 187)

mean_v1 <- mean(v1)

v1[v1 > mean_v1]
greter_than_mean <- v1[v1 > mean_v1]


v1 <- 1:20

