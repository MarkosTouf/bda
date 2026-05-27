import pandas as pd

## Part 1 Lab
Print("Part 1 Lab Session 7.")

#Ingestion  
# Ingest the JSON payload into active RAM
movies = pd.read_json("datasets/Movies.json")


# 1. The Boundaries

# Execute the diagnostic X-ray
print(movies.head(10))

print("------tail 3 rows--------")
print(movies.tail(3))

# 2. The Physical Dimensions
print("\n------shape(rows,columns)")

print(movies.shape)

# 3. The Chemical Makeup (Data Types)
print("\n movies datatypes")
print(movies.dtypes)

# 4. The Mathematical Summary
print("\n numeric summary")
print(movies.describe())

# 5. selected columns
print("\n Selected Columns")

subset = movies[["Title", "Distributor", "Source"]]

print(subset.head())

# 7. filtering
print("\n 7. -----Filtering element:-----------")

filter_long_mv = movies["Running Time min"]>=160

print(filter_long_mv.head())


# 7. filtering
print("\n 8. -----Filtering below:-----------")

long_movies = movies[filter_long_mv]

print(long_movies.head())

print(long_movies[["Running Time min"]])

