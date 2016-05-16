rm(list=ls())
setwd("~/Documents/Github/Dev/ChooseSample")
#dir()
data <- read.csv("R2only.csv",header=T)
#head(data)
library(ggplot2)
dim(data)

#con <- matrix(c(0,39,39,68,68,200,0,39,39,68,68,200),ncol=12)
#conTemp <- matrix(c(0.8,1,0.8,1,0.8,1,0,0.79,0,0.79,0,0.79),ncol=12)
#con <- rbind(con,conTemp)
#con

#make Group1
Group1 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]>0.9)&(data[i,7]<16)){
		Group1 <-rbind(Group1,data[i,])
	}
}
dim(Group1)


#make Group2
Group2 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]>0.9)&(data[i,7]>16)&(data[i,7]<60)){
		Group2 <-rbind(Group2,data[i,])
	}
}
dim(Group2)

#make Group3
Group3 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]>0.9)&(data[i,7]>60)){
		Group3 <-rbind(Group3,data[i,])
	}
}
dim(Group3)

#make Group4
Group4 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]<0.9)&(data[i,7]<16)){
		Group4 <-rbind(Group4,data[i,])
	}
}
dim(Group4)

#make Group5
Group5 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]<0.9)&(data[i,7]>16)&(data[i,7]<60)){
		Group5 <-rbind(Group5,data[i,])
	}
}
dim(Group5)


#make Group6
Group6 = data[FALSE,]
for (i in 1:dim(data)[1]){	
	if ((data[i,16]<0.9)&(data[i,7]>60)){
		Group6 <-rbind(Group6,data[i,])
	}
}
dim(Group6)


#df <- data.frame(matrix(ncol = 3, nrow = 0))
#colnames(df) <- paste0("hello", c(1:3))
#df
#paste0("group",1)

#combin
#rm (plotdata)

#gr = paste0("Group",1)
#ne = eval(parse(text = gr[1]))
#parse(text = gr[1])
#dim(ne)[1]
plotdata = data.frame(matrix(ncol=3,nrow = 0))
#rm(plotdata)
#x <- c()
#y <- c()
#group <- c()
#x <- c(x,ne[0,7])
for (j in 1:6){
	gr = paste0("Group",j)
	ne = eval(parse(text = gr[1]))
	for(i in 1:dim(ne)[1]){
		#x <- c(x,ne[i,7])
		#y <- c(y,ne[i,16])
		#group <- c(group,j)
		temp = c(ne[i,7], ne[i,16],j)
		plotdata = rbind(plotdata,temp)
	}
	#plotdata = 
}
colnames(plotdata) <- c("x", "y","group")
plotdata
class(plotdata)
ggplot(plotdata)+geom_point(aes(x=x,y=y,color=group))+scale_x_continuous(name = "total N : total P ratio",limits=c(0,100))+scale_y_continuous(name = "Cyanobacteria relative abundance",limits=c(0,1))+geom_hline(yintercept = 0.9,linetype="longdash")+geom_hline(yintercept = 0.5,linetype="longdash")+geom_vline(xintercept = 16,linetype="longdash")+geom_vline(xintercept = 60,linetype="longdash")

library(grid)
library(gridExtra)

gr = paste0("Group",6)
ne = eval(parse(text = gr[1]))
p1 <- ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=cyanophyta.ra))
p2 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=chla))
p3 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=secchi))
p4 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=total.carbon))
p5 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=doc))
p6 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=ph))
p7 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=alkalinity))
p8 <-ggplot(ne)+geom_point(aes(x=tn.tp.atomic,y=total.bio))
multiplot(p1,p2,p3,p4,p5,p6,p7,p8,cols=3)

#histogram
ggplot(data, aes(x=cyanophyta.ra))+geom_histogram(binwidth=0.01)+geom_density(fill="blue")


# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)

  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}
