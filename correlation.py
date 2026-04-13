# =============================================================================
# Correlation
# =============================================================================
# Reading the data 
data6 = pd.read_csv(r"E:\Project\29-09-2023.csv",index_col=0)

# data summary
data6.info()

# Copying data to another dataframe
data7 = data6.copy()

# correlating columns of numerical data
numerical_data = data7.select_dtypes(exclude = [object])
corr_matrix = numerical_data.corr()
print(corr_matrix)

data7.describe()
# Setting numerical data to 3 decimal values
pd.set_option("display.float_format",lambda x:"%.3f" % x)
# Checking the datatype of price column
data7.price.dtypes
# Converting int64 to float64
data7.price = data7.price.astype("float64")
# Checking datatype of km_driven
data7.km_driven.dtypes
# Converting int64 to float64
data7.km_driven = data7.km_driven.astype("float64")
data7.info()

# Checking joint probability
pd.crosstab(index = data7.price,columns = data7.km_driven,normalize = True)
sns.boxplot(x = data7.price)
sns.boxplot(x = data7.km_driven)

df_out = remove_outliers(data7, 'price')
number_outliers = data7.shape[0] - df_out.shape[0]
print('Number of outliers:', number_outliers)

sns.boxplot(x = df_out.price)
df_out.info()
df_out.describe()
sns.boxplot(x = df_out.km_driven)
pd.crosstab(index = data7.price,columns = data7.km_driven,normalize = True)

numerical_data = df_out.select_dtypes(exclude = [object])
numerical_data.corr()

pd.crosstab(index = df_out.brand,columns = "count" )
sns.countplot(y = df_out.brand)
sns.countplot(x = df_out.brand,hue = df_out.owner)

df_out.info()

df_out.to_csv(r"E:\Project\30-09-2023.csv")

df_out = pd.read_csv(r"E:\Project\30-09-2023.csv")


