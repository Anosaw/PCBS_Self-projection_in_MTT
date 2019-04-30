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

#Analysis per fictionality

#Analysis per event to projection distance

#Analysis per key order (whether before is left or not)
