data <- read.csv("seaflow_21min.csv", stringsAsFactors = FALSE)

# Question 1
nrow(data[data$pop == 'synecho',])

# Question 2
quantile(data$fsc_small)

datalen <- nrow(data)
index <- sample(1:datalen, datalen/2)
##
# Training and Test data
##
training <- data[index, ]
test <- data[-index, ]

# Question 3
mean(training$time)

# Question 4
ggplot(data, aes(pe, chl_small, color = pop)) + geom_line()

# Question 5,6,7
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=training)
print(model)

# Question 8
# predict.rpart
pred_result_rpart <- rpart:::predict.rpart(model, test, type="class")
sum(pred_result_rpart == test[, "pop"])/length(test[, "pop"])

# Question 9
# predict.randomForest
training$pop <- as.factor(training$pop)
modelRandomForest <- randomForest(fol, data=training)
pred_result_rf <- predict(modelRandomForest, test)
sum(pred_result_rf == test[, "pop"])/length(test[, "pop"])

# Question 10
importance(modelRandomForest)

# Question 11
model_e1071 <- svm(fol, data=training)
pred_result_e1071 <- predict(model_e1071, test)
sum(pred_result_e1071 == test[, "pop"])/length(test[, "pop"])

# Question 11
table(pred = pred_result_rpart, true = test$pop)
table(pred = pred_result_rf, true = test$pop)
table(pred = pred_result_e1071, true = test$pop)

rownames <- c("crypto","nano","pico","synecho","ultra")

df_pred_rpart <- read.table(text = "
  crypto	nano	pico	synecho	ultra
crypto	0	0	0	0	0
nano	46	5035	1	37	646
pico	0	1	9257	0	1816
synecho	0	8	42	9051	108
ultra	0	1421	1072	0	7631
", header = TRUE, row.names = 1)

df_pred_rf <- read.table(text = "
crypto	nano	pico	synecho	ultra
crypto	45	2	0	0	0
nano	0	5584	0	1	332
pico	0	0	10025	0	1376
synecho	1	5	6	9087	7
ultra	0	874	341	0	8486
", header = TRUE, row.names = 1)

df_pred_e1071 <- read.table(text = "
crypto	nano	pico	synecho	ultra
crypto	40	1	0	0	0
nano	2	5660	0	3	369
pico	0	0	10037	27	1347
synecho	4	7	41	9058	7
ultra	0	797	294	0	8478
", header = TRUE, row.names = 1)

sum_predictions <- df_pred_rpart + df_pred_rf + df_pred_e1071

# x <- as.matrix(sum_predictions)
# rc <- rainbow(nrow(x), start = 0, end = .3)
# heatmap(x, Rowv = NA, Colv = NA, 
#         col = heat.colors(256), scale = "column", verbose = T)

# Question 13
# Column 8 in dtaset - fsc_big is not continuous
par(mfrow= c(6,1))
par(mar=c(0,0,0,0)+0.2)
for(i in 6:11) {
#   print(paste(colnames(data)[i], " - ", diff(range(data[,i]))))
  plot(data$cell_id, data[,i])
}

# Question 14
data1 <- data[data$file_id != 208,]

datalen1 <- nrow(data1)
index1 <- sample(1:datalen1, datalen1/2)
##
# Training and Test data after cleaning
##
training1 <- data1[index1, ]
training1$pop <- as.factor(training1$pop)
test1 <- data1[-index1, ]

# SVM
model_e1071_new <- svm(fol, data=training1)
pred_result_e1071_new <- predict(model_e1071_new, test1)
print(paste("Before cleaning data", 
            sum(pred_result_e1071 == test[, "pop"])/length(test[, "pop"])))
print(paste("After Cleaning data", 
            sum(pred_result_e1071_new == test1[, "pop"])/length(test1[, "pop"])))