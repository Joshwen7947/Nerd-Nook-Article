import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('airbnb.csv')

# Initial Exploration 
print(df.head())
print(df.info())
print("Initial Data Shape:",df.shape)
print(df.describe())

# Identify missing and any duplicates
print(df.isnull().sum())
print(df.duplicated().sum())

# Handle missing values by filling with the average
df['reviews_per_month'].fillna(df['reviews_per_month'].mean(), inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df['number_of_reviews'].fillna(df['number_of_reviews'].mean(), inplace=True)

# Drop rows where 'data is still missing & duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Plot histograms for numerical variables
# 1 - Price Vs. Frequency
axs[0, 0].hist(df['price'], bins=20, color="lightblue")
axs[0, 0].set_title('Distribution of Price')
axs[0, 0].set_xlabel('Price')
axs[0, 0].set_ylabel('Frequency')

# 2 - Number of Reviews Vs. Frequency
axs[0, 1].hist(df['number_of_reviews'], bins=20)
axs[0, 1].set_title('Distribution of Number of Reviews')
axs[0, 1].set_xlabel('Number of Reviews')
axs[0, 1].set_ylabel('Frequency')

# 3 - Group by room type and show the average price
room_type_prices = df.groupby('room_type')['price'].mean().reset_index()
axs[0, 2].bar(room_type_prices['room_type'], room_type_prices['price'], color='lightgreen')
axs[0, 2].set_title('Average Price by Room Type')
axs[0, 2].set_xlabel('Room Type')
axs[0, 2].set_ylabel('Average Price')

# 4 - Number of listings in each borough group
neighborhood_counts = df['neighbourhood_group'].value_counts().reset_index()
neighborhood_counts.columns = ['neighbourhood_group', 'count']
axs[1, 0].bar(neighborhood_counts['neighbourhood_group'], neighborhood_counts['count'],color='pink')
axs[1, 0].set_title('Count of Listings by Neighbourhood Group')
axs[1, 0].set_xlabel('Neighbourhood Group')
axs[1, 0].set_ylabel('Count')

# 5 - Scatter to show Price vs. Number of Reviews
axs[1, 1].scatter(df['price'], df['number_of_reviews'],color='purple')
axs[1, 1].set_title('Price vs Number of Reviews')
axs[1, 1].set_xlabel('Price')
axs[1, 1].set_ylabel('Number of Reviews')


# Adjust & show layout (subplot)
plt.tight_layout()
plt.show()

# Identify listings with prices significantly higher than the average
high_price_listings = df[df['price'] > df['price'].mean() + 3 * df['price'].std()]
print("Major Outliers:",high_price_listings)
