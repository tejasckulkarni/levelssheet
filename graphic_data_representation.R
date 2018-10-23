library(rgdal)
library(animation)
library(lubridate)

main.path = "C:/Users/diego/Documents/Leibniz Universitat Hannover/M.Sc. WATENV/II Semester/Research Project/DMap197678/197577DI.shp"
nieder.shp = readOGR(dsn="C:/Users/diego/Documents/Leibniz Universitat Hannover/M.Sc. WATENV/II Semester/Research Project/DMap197678/Niedersachsen_grenze.shp", layer="Niedersachsen_grenze")
gauge.data = readOGR(dsn="C:/Users/diego/Documents/Leibniz Universitat Hannover/M.Sc. WATENV/II Semester/Research Project/DMap197678/gauge_information.shp", layer="gauge_information")
data.index = readOGR(dsn = main.path, layer="197577DI")
output.video = "C:/Users/diego/Documents/Leibniz Universitat Hannover/M.Sc. WATENV/II Semester/Research Project/DMap197678/Video.avi"
start.time = as.Date("19751101", format="%Y%m%d")
end.time   = as.Date("19771031", format="%Y%m%d")
dayly.ts = seq(start.time,end.time, by="day")
num.time.ts = sapply(dayly.ts, function(i) as.numeric(paste0(year(i),
                                                             formatC(month(i), flag=0, width=2), 
                                                             formatC(day(i), flag=0, width=2))))

indexes = data.index@data$SumDeficit
data.time = data.index@data$Year0000
X.coord = data.index@data$X
y.coord = data.index@data$Y
plot(Coord)
plot(X.coord, y.coord, col=index.colors, pch=16)

classify_vector <- function(breakvariable,breakpoints,breakoutput){
  # Generating the colors vector for the station points based on the breakpoints and color data classify_vector <- function(breakvariable, breakpoints, breakoutput){
  output <- breakvariable
  len <- length(breakpoints)
  for(j in 1:length(breakvariable)){
    if(is.na(breakvariable[j])==T) breakvariable[j] <- NA
    else{
      for(i in 1:(len-1)){
        if((breakvariable[j]>=breakpoints[i]) & (breakvariable[j]<breakpoints[(i+1)])){
          output[j] <- breakoutput[i]
        }
      }
      if(breakvariable[j]>breakpoints[len]) output[j] <- breakoutput[len]
    }
  }
  return(output)
}
index.colors = classify_vector(indexes, c(-125699, -3090, -2320,-1547,-773,1), c("red","orange", "yellow", "green", "blue"))

Index.Daily.Info = lapply(num.time.ts, function(i){
  day.index = which(data.time==i)
  x = X.coord[day.index]
  y = y.coord[day.index]
  z = indexes[day.index]
  output = data.frame(x=x, y=y, z=z)
  return(output)
})

graphics.off()
saveVideo({
  par(mfrow=c(1,1),oma=c(1,1,1,1),mar=c(2,2,2,2))
  # STEP 1 - PLOTTING THE STATION DATA
  for(step in 1:length(num.time.ts)){
    plot(nieder.shp)
    plot(gauge.data, pch=16, cex=0.5, col="grey", add=TRUE)
    points(Index.Daily.Info[[step]]$x, Index.Daily.Info[[step]]$y, pch=16, xaxt = "n",yaxt = "n",
           col=classify_vector(Index.Daily.Info[[step]]$z,c(-125699, -3090, -2320,-1547,-773,1), 
                               c("red","orange", "yellow", "green", "blue")))    
    
    title(num.time.ts[step], line=1, cex.main=1)
  }
},video.name=output.video, interval=0.1)
