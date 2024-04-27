
rnorm(100,7,0.5) # creating data simulation

sim = rnorm(100,7,0.5)  # simulated data , creating variable to plot


#pnorm(7.5,7,0,5,lower.tail = TRUE) # to find probability

plot(sim) # returns plot of simuate data

pnorm(7.5,7,0.5,lower.tail = TRUE) # outputs probability consistent with Normal Distribution chart

pnorm(7.5,7,0.5,lower.tail=TRUE) - pnorm(6.5,7,0.5,lower.tail = TRUE) # creating variable for total probability ,we get consistent data with the chart

qnorm(0.95,7,0.5,lower.tail = TRUE) # to construct the X value , value if consistent with chart

