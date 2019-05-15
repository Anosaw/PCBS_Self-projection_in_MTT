#Data importation

p1_01 <- read.table("data/mttexp_01_201904301306.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p1_02 <- read.table("data/mttexp_01_201904301327.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p1_03 <- read.table("data/mttexp_01_201904301346.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p2_01 <- read.table("data/mttexp_02_201905071435.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p2_02 <- read.table("data/mttexp_02_201905071450.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p2_03 <- read.table("data/mttexp_02_201905071501.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p2_04 <- read.table("data/mttexp_02_201905071511.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p3_01 <- read.table("data/mttexp_03_201905071009.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p3_02 <- read.table("data/mttexp_03_201905071019.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p3_03 <- read.table("data/mttexp_03_201905071033.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p3_04 <- read.table("data/mttexp_03_201905071044.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p4_01 <- read.table("data/mttexp_04_201904301002.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p4_02 <- read.table("data/mttexp_04_201904301019.xpd",
                    header = TRUE,
                    sep = ",",
                    skip = 52)

p5_01 <- read.table("data/mttexp_05_201905071005.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p5_02 <- read.table("data/mttexp_05_201905071019.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p5_03 <- read.table("data/mttexp_05_201905071029.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p5_04 <- read.table("data/mttexp_05_201905071040.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p6_01 <- read.table("data/mttexp_06_201905071310.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p6_02 <- read.table("data/mttexp_06_201905071323.xpd",
                   header = TRUE, 
                   sep = ",",
                   skip = 52)

p6_03 <- read.table("data/mttexp_06_201905071337.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p6_04 <- read.table("data/mttexp_06_201905071348.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p7_01 <- read.table("data/mttexp_07_201904301004.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p7_02 <- read.table("data/mttexp_07_201904301023.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p8_01 <- read.table("data/mttexp_08_201905071440.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p8_02 <- read.table("data/mttexp_08_201905071454.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p8_03 <- read.table("data/mttexp_08_201905071508.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p8_04 <- read.table("data/mttexp_08_201905071530.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p12_01 <- read.table("data/mttexp_12_201905141321.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p12_02 <- read.table("data/mttexp_12_201905141331.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p12_03 <- read.table("data/mttexp_12_201905141340.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)

p12_04 <- read.table("data/mttexp_12_201905141348.xpd",
                    header = TRUE, 
                    sep = ",",
                    skip = 52)


data <- rbind(p1_01, p1_02, p1_03,
              p2_01, p2_02, p2_03, p2_04,
              p3_01, p3_02, p3_03, p3_04, 
              p4_01, p4_02,
              p5_01, p5_02, p5_03, p5_04,
              p6_01, p6_02, p6_03, p6_04,
              p7_01, p7_02,
              p8_01, p8_02, p8_03, p8_04,
              p12_01, p12_02, p12_03, p12_04)


#Turn pressed_key into a factor with two levels "right" or "left"
data$pressed_key <- factor(data$pressed_key,
                           levels = c("275", "276"),
                           labels = c("right", "left"),
                           ordered = FALSE)

print(data)
str(data)

#Check if there is any missing data
any(is.na(data))


#General analysis
mean_RT <- mean(data$RT)
sd_RT <- sd(data$RT)

library(plyr)

score_table <- count(data, vars = "good_answer")
print(scrore_table)
str(score_table)

accuracy <- score_table[score_table$good_answer == "True", "freq"] / 
  (score_table[score_table$good_answer == "False", "freq"] + score_table[score_table$good_answer == "True", "freq"])

#Analysis per projection
mean_9past <- mean(data[data$projection == -9, "RT"])
mean_6past <- mean(data[data$projection == -6, "RT"])
mean_3past <- mean(data[data$projection == -3, "RT"])
mean_present <- mean(data[data$projection == 0, "RT"])
mean_3future <- mean(data[data$projection == 3, "RT"])
mean_6future <- mean(data[data$projection == 6, "RT"])
mean_9future <- mean(data[data$projection == 9, "RT"])

sd_9past <- sd(data[data$projection == -9, "RT"])
sd_6past <- sd(data[data$projection == -6, "RT"])
sd_3past <- sd(data[data$projection == -3, "RT"])
sd_present <- sd(data[data$projection == 0, "RT"])
sd_3future <- sd(data[data$projection == 3, "RT"])
sd_6future <- sd(data[data$projection == 6, "RT"])
sd_9future <- sd(data[data$projection == 9, "RT"])

boxplot(data$RT~data$projection,xlab="Projection",ylab="RT")
abline(h=mean(data$RT),lty=2,col="red",lwd=2)

anova_projection <- aov(data$RT~data$projection)
anova_projection
summary(anova_projection)



library("ggplot2")

ggplot(data = data, mapping = aes(x = projection, y = RT, color = fictional)) +
  geom_point() +
  geom_line(mapping = aes(group = fictional))

cleaned_data <- data[data$RT < 4000,]

ggplot(data = cleaned_data, mapping = aes(x = projection, y = RT, color = fictional)) +
  geom_point() +
  geom_line(mapping = aes(group = fictional))

#Analysis per fictionality
mean_fictional <- mean(data[data$fictional == "True", "RT"])
mean_real <- mean(data[data$fictional == "False", "RT"])

sd_fictional <- sd(data[data$fictional == "True", "RT"])
sd_real <- sd(data[data$fictional == "False", "RT"])

boxplot(data$RT~data$fictional,xlab="fictional",ylab="RT")
abline(h=mean(data$RT),lty=2,col="red",lwd=2)

anova_fictionality <- aov(data$RT~data$fictional)
anova_fictionality
summary(anova_fictionality)

#Analysis per event to projection distance



#Analysis per key order (whether before is left or not)
mean_before_is_left <- mean(data[data$before_is_left == "True", "RT"])
mean_before_is_right <- mean(data[data$before_is_left == "False", "RT"])

sd_before_is_left <- sd(data[data$before_is_left == "True", "RT"])
sd_before_is_right <- sd(data[data$before_is_left == "False", "RT"])

boxplot(data$RT~data$before_is_left,xlab="before is left",ylab="RT")
abline(h=mean(data$RT),lty=2,col="red",lwd=2)

anova_key_order <- aov(data$RT~data$before_is_left)
anova_key_order
summary(anova_key_order)

#When taking out wrong answers from questionnaire
