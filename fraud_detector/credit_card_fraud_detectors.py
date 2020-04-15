import argparse
import os 
import pandas as pd

import modules.data_preprocessors as preprocessors
import modules.models as models

# 
# Arguments 
#
def arguments():
    parser = \
        argparse.ArgumentParser(
            description='define',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    # Required arguments
    parser.add_argument(
        "--classifier",
        help='Select one classifier to train the model or to classify the data'
    )
    parser.add_argument(
        "--mode",
        help='\'train\' for training a model OR \'classify\' to classify the data'
    )
    parser.add_argument(
        "--output_folder"
    )
    parser.add_argument(
        "--name"
    )
    parser.add_argument(
        "--data_path",
        default=os.getcwd() + "/data/creditcard.csv"
    )

    args = parser.parse_args()
    return args


#
# Main
#
def main():
    print("Printed")

    args = arguments()
    data_path = os.getcwd() + "/data"
    print(os.listdir(data_path))

    data_df = pd.read_csv(args.data_path)
    print(data_df.dtypes)
    print("Shape of the data:",  data_df.shape)
    #print("data_df.dtypes") 
    
    preprocessors.TrainingDataProcessor.preprocessed_data(df_numerical_data=data_df)

    cl = models.classifier(data_df)
    #random_forest_accuracy = cl.random_forest()
    #ada_boost_accuracy = cl.ada_boost(data_df)
    #cat_boost_accuracy = cl.cat_boost()
    #xg_boost_accuracy = cl.xg_boost()
    svm_accuracy = cl.support_vector_machine()

    #print("Random Forest Accuracy:", random_forest_accuracy)
    #print("Ada Boost Accuracy:", ada_boost_accuracy)
    #print("Cat Boost Accuracy:", cat_boost_accuracy)
    #print("XGBoost Accuracy:", xg_boost_accuracy)
    print("SVM accuracy:", svm_accuracy)


if __name__ == "__main__":
    main()


 
