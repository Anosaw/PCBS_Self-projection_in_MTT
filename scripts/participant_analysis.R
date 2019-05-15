#Script for data importation and participant analysis

library(plyr)


#Data importation
p4_01 <- read.table("data/mttexp_04_201904301002.xpd",
                   header = TRUE, 
                   sep = ",",
                   skip = 52)

p4_02 <- read.table("data/mttexp_04_201904301019.xpd",
                              header = TRUE,
                              sep = ",",
                              skip = 52)

data_p4 <- rbind(p4_01, p4_02)


#Turn pressed_key into a factor with two levels "right" or "left"
data_p4$pressed_key <- factor(data_p4$pressed_key,
                           levels = c("275", "276"),
                           labels = c("right", "left"),
                           ordered = FALSE)

print(data_p4)
str(data_p4)

#Check if there is any missing data
any(is.na(data_p4))

#General analysis
mean_p4 <- mean(data_p4$RT)
sd_p4 <- sd(data_p4$RT)


scoretable_p4 <- count(data_p4, vars = "good_answer")
print(scoretable_p4)
str(scoretable_p4)

accuracy <- scoretable_p4[scoretable_p4$good_answer == "True", "freq"] / 
  (scoretable_p4[scoretable_p4$good_answer == "False", "freq"] + scoretable_p4[scoretable_p4$good_answer == "True", "freq"])
