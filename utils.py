import pandas as pd

def read_data(full_data: bool = False, balanced: bool = False) -> pd.DataFrame:
    if full_data:
        df = pd.read_csv('../data/US_Accidents_March23.csv')
        if balanced:
            min_samples = df['Severity'].value_counts().min()
            balanced_data = pd.DataFrame()

            for severity_type in df['Severity'].unique():
                sampled_data = df[df['Severity'] == severity_type].sample(min_samples, replace=False)
                balanced_data = pd.concat([balanced_data, sampled_data])

            balanced_data = balanced_data.sample(frac=1).reset_index(drop=True)

            return balanced_data
        return df
        
    return pd.read_csv('../data/US_Accidents_March23_sampled_500k.csv') 

