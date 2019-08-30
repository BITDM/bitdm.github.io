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
        self.n_sim_user = 20
        self.n_rec_movie = 10
        self.train_set = {}
        self.test_set = {}

        self.user_sim_matrix = {}
        self.movie_count = 0

        self.movie_pop = {}
        self.movie_sim = {}
        print('Similar user number = %d' % self.n_sim_user)
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


    #电影的流行度
    def cal_movie_popularity(self):
        for user, movies in self.train_set.items():
            for movie in movies:
                if movie not in self.movie_pop:
                    self.movie_pop[movie] = 0
                self.movie_pop[movie] += 1

    #电影之间相似度
    def cal_movie_sim(self):
        for user, movies in self.train_set.items():
            for movie1 in movies:
                self.movie_sim.setdefault(movie1, defaultdict(int))
                for movie2 in movies:
                    if movie2 == movie1:
                        continue
                    self.movie_sim[movie1][movie2] += 1

    #计算用户之间的相似度
    def cal_user_sim1(self):

        for user1, movies1 in self.train_set.items():
            self.user_sim_matrix.setdefault(user1, defaultdict(int))
            for user2, movies2 in self.train_set.items():
                if user1 == user2:
                    continue
                for movie in movies1:
                    if movie in movies2:
                        self.user_sim_matrix[user1][user2] += 1
        self.movie_count = 8713

    #使用item-user倒排表，降低计算复杂度
    #并且对热度进行惩罚
    def cal_user_sim2(self):

        #先建立item-user倒排表
        print('>>>Building movie-user table ...')
        movie_user = {}
        for user, movies in self.train_set.items():
            for movie in movies:
                if movie not in movie_user:
                    movie_user[movie] = set()
                movie_user[movie].add(user)
        print('>>>Build movie-user table success!')


        #the total count of movies in the training set
        self.movie_count = len(movie_user)
        print('>>>Total movie number = %d' % self.movie_count)

        #the count of common movies of u and v
        print('>>>Build user co-rated movies matrix ...')
        for movie, users in movie_user.items():
            for u in users:
                self.user_sim_matrix.setdefault(u, defaultdict(int))
                for v in users:
                    if u==v:
                        continue
                    self.user_sim_matrix[u][v] += 1

        print('>>>Build user co-rated movies matrix success!')

        # calculate the similarity of u and v
        print('>>>Calculating user similarity matrix ...')
        for u, related_users in self.user_sim_matrix.items():
            for v, count in related_users.items():
                self.user_sim_matrix[u][v] = count / math.sqrt(len(self.train_set[u]) * len(self.train_set[v]))
        print('>>>Calculate user similarity matrix success!')

    #给出对user的推荐电影
    def recommend(self, user):
        #取前K个最相似用户
        K = self.n_sim_user
        #推荐N部电影
        N = self.n_rec_movie
        #rank中存放电影以及用户user对电影的预测评分
        rank = {}
        watched_movies = self.train_set[user]
        for v, wuv in sorted(self.user_sim_matrix[user].items(), key=itemgetter(1), reverse=True)[0:K]:
            for i, rvi in self.train_set[v].items():
                if i in watched_movies:
                    continue
                rank.setdefault(i, 0)
                rank[i] += wuv * rvi

        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]

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
    userCF.cal_user_sim2()
    userCF.evaluate()

#precisioin=0.2997	recall=0.0722	coverage=0.0365