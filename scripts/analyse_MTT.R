#Data importation
mtt4 <- read.table("data/mttexp_04_201904301002.xpd",
                   header = TRUE, 
                   sep = ",",
                   skip = 52)

print(mtt4)
str(mtt4)

#Turn pressed_key into a factor with two levels "right" or "left"
mtt4$pressed_key <- factor(mtt4$pressed_key,
                           levels = c("275", "276"),
                           labels = c("right", "left"),
                           ordered = FALSE)

print(mtt4)
str(mtt4)

#Check if there is any missing data
any(is.na(mtt4))


#General analysis
mean_RT = mean(mtt4$RT)
sd_RT = sd(mtt4$RT)

#Analysis per projection
mean_9past <- mean(mtt4[mtt4$projection == -9, "RT"])
mean_6past <- mean(mtt4[mtt4$projection == -6, "RT"])
mean_3past <- mean(mtt4[mtt4$projection == -3, "RT"])
mean_present <- mean(mtt4[mtt4$projection == 0, "RT"])
mean_3future <- mean(mtt4[mtt4$projection == 3, "RT"])
mean_6future <- mean(mtt4[mtt4$projection == 6, "RT"])
mean_9future <- mean(mtt4[mtt4$projection == 9, "RT"])

sd_9past <- sd(mtt4[mtt4$projection == -9, "RT"])
sd_6past <- sd(mtt4[mtt4$projection == -6, "RT"])
sd_3past <- sd(mtt4[mtt4$projection == -3, "RT"])
sd_present <- sd(mtt4[mtt4$projection == 0, "RT"])
sd_3future <- sd(mtt4[mtt4$projection == 3, "RT"])
sd_6future <- sd(mtt4[mtt4$projection == 6, "RT"])
sd_9future <- sd(mtt4[mtt4$projection == 9, "RT"])

#Analysis per fictionality
mean_fictional <- mean(mtt4[mtt4$fictional == "True", "RT"])
mean_real <- mean(mtt4[mtt4$fictional == "False", "RT"])

sd_fictional <- sd(mtt4[mtt4$fictional == "True", "RT"])
sd_real <- sd(mtt4[mtt4$fictional == "False", "RT"])

#Analysis per event to projection distance

#Analysis per key order (whether before is left or not)
mean_before_is_left <- mean(mtt4[mtt4$before_is_left == "True", "RT"])
mean_before_is_right <- mean(mtt4[mtt4$before_is_left == "False", "RT"])

sd_before_is_left <- sd(mtt4[mtt4$before_is_left == "True", "RT"])
sd_before_is_right <- sd(mtt4[mtt4$before_is_left == "False", "RT"])
