from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from catboost import CatBoostClassifier
import xgboost as xgb
from sklearn import svm
import matplotlib
import matplotlib.pyplot as plt

class classifier: 
    def __init__(self, data_df):        
        self.data_df = data_df

    target = 'Class'
    predictors = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',\
        'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',\
        'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',\
        'Amount']
    
    
    RANDOM_STATE = 2019
    #TRAIN/VALIDATION/TEST SPLIT
    #VALIDATION
    VALID_SIZE = 0.20 # simple validation using train_test_split
    TEST_SIZE = 0.20 # test size using_train_test_split
    NUM_ESTIMATORS = 100

    #CROSS-VALIDATION
    NUMBER_KFOLDS = 5 #number of KFolds for cross-validation

    MAX_ROUNDS = 10 #lgb iterations
    EARLY_STOP = 50 #lgb early stop 
    OPT_ROUNDS = 1000  #To be adjusted based on best validation rounds
    VERBOSE_EVAL = 50 #Print out metric result
    

    def data_split(self):
        train_df, test_df = train_test_split(self.data_df, test_size=self.TEST_SIZE, \
            random_state=self.RANDOM_STATE, shuffle=True )
        train_df, valid_df = train_test_split(train_df, test_size=self.VALID_SIZE, \
            random_state=self.RANDOM_STATE, shuffle=True )

        return train_df, test_df, valid_df

        
    def random_forest(self):
        RFC_METRIC = 'gini'  #metric used for RandomForrestClassifier
        NUM_ESTIMATORS = 100 #number of estimators used for RandomForrestClassifier
        NO_JOBS = 4 #number of parallel jobs used for RandomForrestClassifier

        train_df, test_df, valid_df = self.data_split()

        clf = RandomForestClassifier(n_jobs=NO_JOBS, 
                                    random_state=self.RANDOM_STATE,
                                    criterion=RFC_METRIC,
                                    n_estimators=NUM_ESTIMATORS,
                                    verbose=False)

        clf.fit(train_df[self.predictors], train_df[self.target].values)
        preds = clf.predict(valid_df[self.predictors])
        accuracy = roc_auc_score(valid_df[self.target].values, preds)

        return accuracy


    def ada_boost(self):
        train_df, test_df, valid_df = self.data_split()

        clf = AdaBoostClassifier(random_state=self.RANDOM_STATE,
                         algorithm='SAMME.R',
                         learning_rate=0.8,
                             n_estimators=self.NUM_ESTIMATORS)

        clf.fit(train_df[self.predictors], train_df[self.target].values)
        preds = clf.predict(valid_df[self.predictors])
        accuracy = roc_auc_score(valid_df[self.target].values, preds)

        return accuracy


    def cat_boost(self):
        train_df, test_df, valid_df = self.data_split()

        clf = CatBoostClassifier(iterations=500,
                                    learning_rate=0.02,
                                    depth=12,
                                    eval_metric='AUC',
                                    random_seed = self.RANDOM_STATE,
                                    bagging_temperature = 0.2,
                                    od_type='Iter',
                                    metric_period = self.VERBOSE_EVAL,
                                    od_wait=100)

        clf.fit(train_df[self.predictors], train_df[self.target].values,verbose=True)
        preds = clf.predict(valid_df[self.predictors])
        accuracy = roc_auc_score(valid_df[self.target].values, preds)

        return accuracy


    def xg_boost(self):
        train_df, test_df, valid_df = self.data_split()
        # Prepare the train and valid datasets
        dtrain = xgb.DMatrix(train_df[self.predictors], train_df[self.target].values)
        dvalid = xgb.DMatrix(valid_df[self.predictors], valid_df[self.target].values)
        dtest = xgb.DMatrix(test_df[self.predictors], test_df[self.target].values)

        #What to monitor (in this case, **train** and **valid**)
        watchlist = [(dtrain, 'train'), (dvalid, 'valid')]

        # Set xgboost parameters
        params = {}
        params['objective'] = 'binary:logistic'
        params['eta'] = 0.039
        params['silent'] = True
        params['max_depth'] = 2
        params['subsample'] = 0.8
        params['colsample_bytree'] = 0.9
        params['eval_metric'] = 'auc'
        params['random_state'] = self.RANDOM_STATE

        model = xgb.train(params, 
                dtrain, 
                self.MAX_ROUNDS, 
                watchlist, 
                early_stopping_rounds=self.EARLY_STOP, 
                maximize=True, 
                verbose_eval=self.VERBOSE_EVAL)

        preds = model.predict(dtest)
        roc_auc_score(test_df[self.target].values, preds)

        fig, (ax) = plt.subplots(ncols=1, figsize=(8,5))
        xgb.plot_importance(model, height=0.8, title="Features importance (XGBoost)", \
            ax=ax, color="green") 
        plt.show()


    def support_vector_machine(self):
        train_df, test_df, valid_df = self.data_split()
        #print("train_df", train_df.head())
        #print("test_df", test_df.head())
        
        clf = svm.SVC(kernel='linear', C=0.01)
        clf.fit(train_df[self.predictors], train_df[self.target].values)
        preds = clf.predict(valid_df[self.predictors])
        accuracy = roc_auc_score(valid_df[self.target].values, preds)

        return accuracy