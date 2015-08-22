library(infuser)
args <- commandArgs(TRUE)
X <- as.character(args[1])
timestamp <- format(as.Date(X,"%Y-%m-%d"),"%Y%m%d")

DO AWESOME THINGS

write.csv(YOUREAWESOME,file=paste0('awesome_is_here_',timestamp,'.txt'),row.names=F)