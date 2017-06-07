# 数据挖掘第一次作业
# 何果财
# 2120160995

# read datasets
setwd("C:\\Users\\hegc\\Desktop\\作业\\数据挖掘\\first_home_work")
horse.colic.train = read.table('datasets/horse-colic.data', 
			header=F, sep=" ",
			col.names=c('surgery', 'Age', 'Hospital Number', 'rectal temperature', 'pulse', 'respiratory rate', 
					'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time',
					 'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube', 'nasogastric reflux', 
					'nasogastric reflux PH', 'rectal examination feces', 'abdomen', 'packed cell volume', 
					'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 
					'surgical lesion', 'type of lesion 1', 'type of lesion 2', 'type of lesion 3', 'cp_data'))
horse.colic.test = read.table('datasets/horse-colic.test', 
			header=F, sep=" ",
			col.names=c('surgery', 'Age', 'Hospital Number', 'rectal temperature', 'pulse', 'respiratory rate', 
					'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time', 
					'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube', 'nasogastric reflux', 
					'nasogastric reflux PH', 'rectal examination feces', 'abdomen', 'packed cell volume', 
					'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 
					'surgical lesion', 'type of lesion 1', 'type of lesion 2', 'type of lesion 3', 'cp_data')
			)

horse.colic = rbind(horse.colic.train, horse.colic.test)
str(horse.colic)
# 修改数据帧的数据类型

horse.colic$Hospital.Number = as.character(horse.colic$Hospital.Number)
horse.colic$rectal.temperature = as.double(as.character(horse.colic$rectal.temperature))
horse.colic$pulse= as.integer(as.character(horse.colic$pulse))
horse.colic$respiratory.rate= as.integer(as.character(horse.colic$respiratory.rate))
horse.colic$nasogastric.reflux.PH= as.double(as.character(horse.colic$nasogastric.reflux.PH))
horse.colic$packed.cell.volume= as.double(as.character(horse.colic$packed.cell.volume))
horse.colic$total.protein= as.numeric(as.character(horse.colic$total.protein))
horse.colic$abdomcentesis.total.protein= as.numeric(as.character(horse.colic$abdomcentesis.total.protein))
horse.colic$surgical.lesion= as.factor(horse.colic$surgical.lesion)
horse.colic$type.of.lesion.1= as.factor(horse.colic$type.of.lesion.1)
horse.colic$type.of.lesion.2= as.factor(horse.colic$type.of.lesion.2)
horse.colic$type.of.lesion.3= as.factor(horse.colic$type.of.lesion.3)
horse.colic$cp_data= as.factor(horse.colic$cp_data)

# 修改Age列错误值9->>2
horse.colic$Age[horse.colic$Age== 9]<-2
horse.colic$Age = as.factor(horse.colic$Age)

# 摘要
summary(horse.colic)

# 加载绘图库
library(car)

func.hist = function(x, main='hist of x', xlab='x', ylab='freq'){
	# 绘制直方图
	windows()
	hist(x, main=main, xlab=xlab, ylab=ylab)
}

func.qq = function(x, main='norm qq Plot of x', ylab='x'){
	# 绘制QQ图
	windows()
	qqPlot(x, main=main, ylab=ylab)
}

func.box = function(x, main='box of x', ylab='x'){
	#绘制盒图
	#ylab为设置y轴标题；
	#rug函数绘制变量的实际值，side=4表示绘制在图的右侧（1在下方，2在左侧，3在上方）；
	#abline函数绘制水平线，mean表示均值，na.rm=T指计算时不考虑NA值，lty=2设置线型为虚线。
	windows()
	boxplot(x, main=main, ylab=ylab)
	rug(x,side=4)
	abline(h=mean(x, na.rm=T),lty=2)
}

func.hist(as.numeric(horse.colic$rectal.temperature), main='hist of rectal temperature', xlab='rectal temperature')
func.qq(as.numeric(horse.colic$rectal.temperature), main='Norm qq Plot of rectal temperature', ylab='rectal temperature')
func.box(as.numeric(horse.colic$rectal.temperature), main='box of rectal temperature', ylab='rectal temperature')

func.hist(as.numeric(horse.colic$pulse), main='hist of pulse', xlab='pulse')
func.qq(as.numeric(horse.colic$pulse), main='norm qq Plot of pulse', ylab='pulse')
func.box(as.numeric(horse.colic$pulse), main='box of pulse', ylab='pulse')

# 数据缺损的处理

# 1. 剔除缺失数据
library(DMwR)
# '?' 转换为NA
func.uniform_defect_to_NA <- function(){
	temp = horse.colic
	rowid = 1
	len = nrow(temp)
	repeat{
		row = temp[rowid,]
		if("?" %in% as.character(t(row))){
			#print(as.character(t(row)))
			#temp <- temp[-rowid,]
			temp[rowid,][temp[rowid,] == '?'] = NA
			#next
		}
		if(rowid > len){
			break
		}
		rowid = rowid + 1
	}
	return(temp)
}

# 去除NA, 若全部去除，则只剩7个数据点， 选择多于20%的NA值得行删除
horse.colic.omit = func.uniform_defect_to_NA()
#horse.colic.omit = na.omit(horse.colic.omit)
horse.colic.omit<-horse.colic.omit[-manyNAs(horse.colic.omit),]

# 写入文件
write.table(horse.colic.omit,'horse.colic.omit', col.names = F, row.names = F, quote = F)

# 以rectal temperature 为例进行omit前后可视化对比
func.hist(as.numeric(horse.colic$rectal.temperature), main='hist of rectal temperature with no omit', xlab='rectal temperature')
func.qq(as.numeric(horse.colic$rectal.temperature), main='Norm qq Plot of rectal temperature with no omit', ylab='rectal temperature')
func.box(as.numeric(horse.colic$rectal.temperature), main='box of rectal temperature with no omit', ylab='rectal temperature')

func.hist(as.numeric(horse.colic.omit$rectal.temperature), main='hist of rectal temperature with omit', xlab='rectal temperature')
func.qq(as.numeric(horse.colic.omit$rectal.temperature), main='Norm qq Plot of rectal temperature with omit', ylab='rectal temperature')
func.box(as.numeric(horse.colic.omit$rectal.temperature), main='box of rectal temperature with omit', ylab='rectal temperature')


# 2. 用最高频率值来填补缺失值
horse.colic.max_freq_fill = func.uniform_defect_to_NA()
horse.colic.max_freq_fill= centralImputation(horse.colic.max_freq_fill)
write.table(horse.colic.max_freq_fill, 'horse.colic.max_freq_fill',col.names = F,row.names = F, quote = F)

# 以rectal temperature 为例进行max_freq_fill前后可视化对比
func.hist(as.numeric(horse.colic$rectal.temperature), main='hist of rectal temperature with no max_freq_fill', xlab='rectal temperature')
func.qq(as.numeric(horse.colic$rectal.temperature), main='Norm qq Plot of rectal temperature with no max_freq_fill', ylab='rectal temperature')
func.box(as.numeric(horse.colic$rectal.temperature), main='box of rectal temperature with no max_freq_fill', ylab='rectal temperature')

func.hist(as.numeric(horse.colic.omit$rectal.temperature), main='hist of rectal temperature with max_freq_fill', xlab='rectal temperature')
func.qq(as.numeric(horse.colic.omit$rectal.temperature), main='Norm qq Plot of rectal temperature with max_freq_fill', ylab='rectal temperature')
func.box(as.numeric(horse.colic.omit$rectal.temperature), main='box of rectal temperature with max_freq_fill', ylab='rectal temperature')

# 3. 通过属性的相关关系来填补缺失值

horse.colic.col_relative_fill = func.uniform_defect_to_NA()

symnum(cor(horse.colic.col_relative_fill[, 4:24],use='complete.obs'))
lm(formula=pulse~respiratory.rate, data=horse.colic.col_relative_fill)
col_relative_fill <- function(pulse){
	if(is.na(pulse))
		return(NA)
	else return (48.0187 + 0.7086 * pulse)
}
horse.colic.col_relative_fill[is.na(horse.colic.col_relative_fill$pulse),'pulse'] <- sapply(horse.colic.col_relative_fill[is.na(horse.colic.col_relative_fill$pulse),
															'respiratory.rate'],col_relative_fill)
write.table(horse.colic.col_relative_fill,'horse.colic.col_relative_fill',col.names = F,row.names = F, quote = F)

# 以pulse 为例进行col_relative_fill前后可视化对比
func.hist(as.numeric(horse.colic$pulse), main='hist of pulse with no col_relative_fill', xlab='pulse')
func.qq(as.numeric(horse.colic$pulse), main='Norm qq Plot of pulse with no col_relative_fill', ylab='pulse')
func.box(as.numeric(horse.colic$pulse), main='box of pulse with no col_relative_fill', ylab='pulse')

func.hist(as.numeric(horse.colic.col_relative_fill$pulse), main='hist of pulse with col_relative_fill', xlab='pulse')
func.qq(as.numeric(horse.colic.col_relative_fill$pulse), main='Norm qq Plot of pulse with col_relative_fill', ylab='pulse')
func.box(as.numeric(horse.colic.col_relative_fill$pulse), main='box of pulse with col_relative_fill', ylab='pulse')


#4. 通过数据对象之间的相似型来填补缺失值

horse.colic.data_obj_similarity_fill = func.uniform_defect_to_NA()
horse.colic.data_obj_similarity_fill = knnImputation(horse.colic.data_obj_similarity_fill, k=10)
write.table(horse.colic.data_obj_similarity_fill,'horse.colic.data_obj_similarity_fill',col.names = F,row.names = F, quote = F)

func.hist(as.numeric(horse.colic$rectal.temperature), main='hist of rectal temperature with no data_obj_similarity_fill', xlab='rectal temperature')
func.qq(as.numeric(horse.colic$rectal.temperature), main='Norm qq Plot of rectal temperature with no data_obj_similarity_fill', ylab='rectal temperature')
func.box(as.numeric(horse.colic$rectal.temperature), main='box of rectal temperature with no data_obj_similarity_fill', ylab='rectal temperature')

func.hist(as.numeric(horse.colic.data_obj_similarity_fill$rectal.temperature), main='hist of rectal temperature with data_obj_similarity_fill', xlab='rectal temperature')
func.qq(as.numeric(horse.colic.data_obj_similarity_fill$rectal.temperature), main='Norm qq Plot of rectal temperature with data_obj_similarity_fill', ylab='rectal temperature')
func.box(as.numeric(horse.colic.data_obj_similarity_fill$rectal.temperature), main='box of rectal temperature with data_obj_similarity_fill', ylab='rectal temperature')


