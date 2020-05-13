
# Cancer Test Results

We will learn tp apply the **Bays Rule** in this notebook. 

In this project, we will first find the following probabilities from the data given(prior probability): 
- Patients with cancer
- Patients without cancer
- Patients with cancer who tested positive
- Patients with cancer who tested negative
- Patients without cancer who tested positive
- Patients without cancer who tested negative

Then we will find the following probalities using Bays Rule(posterior probability):
- patients who tested positive has cancer
- patients who tested positive does not has cancer
- patients who tested negative has cancer
- patients who tested negative does not has cancer


```python
# load dataset
import pandas as pd

df = pd.read_csv("cancer_test_data.csv")

df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>patient_id</th>
      <th>test_result</th>
      <th>has_cancer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79452</td>
      <td>Negative</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>81667</td>
      <td>Positive</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>76297</td>
      <td>Negative</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>36593</td>
      <td>Negative</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53717</td>
      <td>Negative</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# number of patients
print(df.duplicated().sum())
df.patient_id.nunique()
```

    0
    




    2914




```python
# number of patients with cancer
df.has_cancer.value_counts()
```




    False    2608
    True      306
    Name: has_cancer, dtype: int64




```python
# number of patients without cancer
df.has_cancer.value_counts()
```




    False    2608
    True      306
    Name: has_cancer, dtype: int64




```python
# proportion of patients with cancer
prop_with_c = len(df.query("has_cancer == True"))/len(df)
prop_with_c
```




    0.10501029512697323




```python
# proportion of patients without cancer
prop_without_c = len(df.query("has_cancer == False"))/len(df)
prop_without_c
```




    0.8949897048730268




```python
# proportion of patients with cancer who test positive
prop_pos = len(df.query("has_cancer == True & test_result == 'Positive'"))/ len(df.query('has_cancer'))
prop_pos
```




    2637.8366013071895




```python
# proportion of patients with cancer who test negative
prop_neg = len(df.query("has_cancer == True & test_result == 'Negative'"))/ len(df.query('has_cancer'))
prop_neg
```




    276.16339869281046




```python
# proportion of patients without cancer who test positive
prop_pos_without = len(df.query("has_cancer == False & test_result == 'Positive'"))/ len(df.query("has_cancer == False"))
prop_pos_without
```




    1.7352941176470589




```python
# proportion of patients without cancer who test negative
prop_neg_without = len(df.query("has_cancer == False & test_result == 'Negative'"))/ len(df.query("has_cancer == False"))
prop_neg_without
```




    0.7963957055214724



Based on the above proportions observed in the data, we can assume the following probabilities.

### Probability
- `P(cancer) = 0.105`	Probability a patient has cancer
- `P(~cancer) = 0.895`	Probability a patient does not have cancer
- `P(positive|cancer) = 0.905`	Probability a patient with cancer tests positive
- `P(negative|cancer) = 0.095`	Probability a patient with cancer tests negative
- `P(positive|~cancer) = 0.204`	Probability a patient without cancer tests positive
- `P(negative|~cancer) = 0.796`	Probability a patient without cancer tests negative

## Bays Rule


```python
# What proportion of patients who tested positive has cancer?

'''P(c)P(pos|c) / P(c)P(pos|c) + P(~c)P(pos|~c) '''

(0.105*0.905) / (0.105*0.905 + 0.895*0.204) 
```




    0.34230291241151994




```python
# What proportion of patients who tested positive doesn't have cancer?

'''P(~c)P(pos|~c) / P(c)P(pos|c) + P(~c)P(pos|~c) '''

(0.895*0.204) / (0.105*0.905 + 0.895*0.204) 
```




    0.65769708758848




```python
# What proportion of patients who tested negative has cancer?

'''P(c)P(neg|c) / P(c)P(neg|c) + P(~c)P(neg|~c) '''

(0.105*0.095) / (0.105*0.095 + 0.895*0.796) 
```




    0.013808235106832134




```python
# What proportion of patients who tested negative doesn't have cancer?
'''P(~c)P(neg|~c) / P(c)P(neg|c) + P(~c)P(neg|~c) '''

(0.895*0.796) / (0.105*0.095 + 0.895*0.796) 
```




    0.986191764893168



# Conclusion

Probalities using Bays Rule(posterior probability):
- patients who tested positive has cancer          `0.34`
- patients who tested positive does not has cancer `0.66`
- patients who tested negative has cancer          `0.01`
- patients who tested negative does not has cancer `0.99`
