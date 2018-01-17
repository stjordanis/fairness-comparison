from algorithms.kamishima.KamishimaAlgorithm import KamishimaAlgorithm
from algorithms.feldman.FeldmanAlgorithm import FeldmanAlgorithm
from algorithms.baseline.SVM import SVM
from algorithms.baseline.DecisionTree import DecisionTree
from algorithms.baseline.GaussianNB import GaussianNB
from algorithms.baseline.LogisticRegression import LogisticRegression
from algorithms.ParamGridSearch import ParamGridSearch

from metrics.DisparateImpact import DisparateImpact
from metrics.Accuracy import Accuracy
from metrics.MCC import MCC

ALGORITHMS = [ SVM(), GaussianNB(), LogisticRegression(), DecisionTree(),     # baseline
               KamishimaAlgorithm(),                                          # Kamishima
               ParamGridSearch(KamishimaAlgorithm(), Accuracy()),             # Kamishima params
               ParamGridSearch(KamishimaAlgorithm(), DisparateImpact()),
               FeldmanAlgorithm(SVM()), FeldmanAlgorithm(GaussianNB()),       # Feldman
               FeldmanAlgorithm(LogisticRegression()), FeldmanAlgorithm(DecisionTree()),
               ParamGridSearch(FeldmanAlgorithm(SVM()), DisparateImpact()),   # Feldman params
               ParamGridSearch(FeldmanAlgorithm(SVM()), Accuracy()),
               ParamGridSearch(FeldmanAlgorithm(GaussianNB()), DisparateImpact()),
               ParamGridSearch(FeldmanAlgorithm(GaussianNB()), Accuracy())
             ]
