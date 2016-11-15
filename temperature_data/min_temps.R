# script for getting to using t.test() just for getting a
# 100(1-alpha)% CI (see my Jupyter notebook for more details)

# read in the MSP airport January 1 min temperature data file
dat = read.csv('min_temps.txt',header=TRUE)

# Assume these 70 temperature measurements x_1, x_2, ..., x_70
# are independent of each other.

# Check if it is reasonable to these measurements are all realizations
# from the same distribution

# 1. make a time plot-- I see a bit of a declining trend, not totally flat
plot(dat$year,dat$minTemp,type = 'o', xlab='year', ylab='Min temp (F)')

# 2. do some histogramming-- play with # of breaks!
hist(dat$minTemp,breaks = 10,freq = FALSE)

# 3. qq-plot-- the quantiles of dat$minTemp are how many of the values
#     lie below a certain percentage.  Plot those against the quantiles
#     of a std normal dist to get a sense for whether the data are from
#     a normal distribution
qqnorm(dat$minTemp)
qqline(dat$minTemp)

# To get a sense for how much that plot supports dat$minTemp coming from
# a normal distribution, compare a plot for a sample of the same size
# generated with rnorm and similarly plotted.
mu = mean(dat$minTemp)
sig = sd(dat$minTemp)
x = rnorm(80, mu, sig)
qqnorm(x)
qqline(x)
# Our sample is arguably as consistent with a random sample of size 80
# from a normal distribution.


# Well, it's probably not too far from normally dist'd, proceed to t-test
mean(dat$minTemp)
sd(dat$minTemp)
t.test(x=dat$minTemp, conf.level = 0.90)
