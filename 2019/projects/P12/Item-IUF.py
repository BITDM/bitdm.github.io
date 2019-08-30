import random
import math
import os
from operator import itemgetter
import pandas as pd

from collections import defaultdict

random.seed(0)

filename = 'ml-latest-small/ratings.csv'
class UserBasedCF:
    def __init__(self):
        self.n_sim_items = 20
        self.n_rec_movie = 5
        self.train_set = {}
        self.test_set = {}

        self.item_sim_matrix = {}
        self.movie_count = 0

        self.movie_pop = {}
        self.movie_sim = {}
        print('Similar items number = %d' % self.n_sim_items)
        print('Recommneded movie number = %d' % self.n_rec_movie)

    def load_data(self, file, pivot=0.75):
        train_set_len = 0
        test_set_len = 0
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            user, movie, rating = row['userId'], row['movieId'], row['rating']
            if random.random() < pivot:
                self.train_set.setdefault(user, {})
                self.train_set[user][movie] = int(rating)
                train_set_len += 1
            else:
                self.test_set.setdefault(user, {})
                self.test_set[user][movie] = int(rating)
                test_set_len += 1

        print('>>>Split trainingSet and testSet success!')
        print('TrainSet = %s' % train_set_len)
        print('TestSet = %s' % test_set_len)

    def ItemSimilarity(self):
        #train_set已经是user-item倒排表
        print("用户数量为：%d" %len(self.train_set))
        N = {}
        #计算物品i和物品j被同时喜欢的次数
        for user, items in self.train_set.items():
            for i in items:
                N.setdefault(i, 0)
                N[i] += 1
                self.item_sim_matrix.setdefault(i, defaultdict(int))
                for j in items:
                    if i==j:
                        continue
                    self.item_sim_matrix[i][j] += 1.0 / math.log(1 + len(items))
        # print('>>>未归一化的物品相似度矩阵为：')
        # print(self.item_sim_matrix)
        for i, related_items in self.item_sim_matrix.items():
            maxWij = related_items[max(related_items, key=related_items.get)]
            for j, wij in related_items.items():
                related_items[j] = wij/maxWij
        # print(">>>归一化过后的物品相似度矩阵为：")
        # print(self.item_sim_matrix)
        self.movie_count = len(self.item_sim_matrix)
        print("电影的总数量为：%d" %self.movie_count)

        for i, related_items in self.item_sim_matrix.items():
            for j, rij in related_items.items():
                self.item_sim_matrix[i][j] = self.item_sim_matrix[i][j]/math.sqrt(N[i] * N[j])



    def recommend(self, user):
        #取前K个最相似items
        K = self.n_sim_items
        #推荐N部电影
        N = self.n_rec_movie
        #rank中存放电影以及用户user对电影的预测评分
        rank = {}
        watched_movies = self.train_set[user]
        for movie, rating in watched_movies.items():
            for related_movie, similarity_factor in sorted(self.item_sim_matrix[movie].items(), key=itemgetter(1), reverse=True)[:K]:
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += similarity_factor * rating
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]


    def evaluate(self):
        print(">>>Evaluation start ...")
        N = self.n_rec_movie
        # 准确率和召回率
        hit = 0
        rec_count = 0
        test_count = 0
        # 覆盖率
        all_rec_movies = set()

        #对所有user都进行推荐
        for i, user in enumerate(self.train_set):
            test_movies = self.test_set.get(user, {})
            rec_movies = self.recommend(user)
            for movie, w in rec_movies:
                if movie in test_movies:
                    hit += 1
                all_rec_movies.add(movie)
            rec_count += N
            test_count += len(test_movies)

        precision = hit / (1.0 * rec_count)
        recall = hit / (1.0 * test_count)
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        print('precisioin=%.4f\trecall=%.4f\tcoverage=%.4f' % (precision, recall, coverage))

if __name__ == '__main__':
    filename = 'ml-latest-small/ratings.csv'
    userCF = UserBasedCF()
    userCF.load_data(filename)
    userCF.ItemSimilarity()
    userCF.evaluate()